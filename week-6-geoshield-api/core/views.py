from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.utils import timezone
import geoip2.database
import ipaddress
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from developers.authentication import APIKeyAuthentication
from developers.serializers import IPAnalyzeSerializer
from billing.stripe_utils import record_usage
from django.shortcuts import redirect

def home(request):
    return redirect('/swagger/')

response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "ip": openapi.Schema(type=openapi.TYPE_STRING),
        "country": openapi.Schema(type=openapi.TYPE_STRING),
        "city": openapi.Schema(type=openapi.TYPE_STRING),
        "latitude": openapi.Schema(type=openapi.TYPE_NUMBER),
        "longitude": openapi.Schema(type=openapi.TYPE_NUMBER),
        "isp": openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
        "risk_score": openapi.Schema(type=openapi.TYPE_INTEGER),
        "monthly_usage": openapi.Schema(type=openapi.TYPE_INTEGER),
        "free_requests_remaining": openapi.Schema(type=openapi.TYPE_INTEGER),
    }
)


class IPAnalyzeView(APIView):
    authentication_classes = [APIKeyAuthentication]

    @swagger_auto_schema(
        request_body=IPAnalyzeSerializer,
        responses={200: response_schema},
        operation_description="Analyze an IP address and return geolocation and risk score."
    )

    def post(self, request):
        # Validate input with serializer
        serializer = IPAnalyzeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        ip = serializer.validated_data.get("ip")

        # Fallback to client IP if none provided
        if not ip:
            ip = request.META.get("HTTP_X_FORWARDED_FOR") or request.META.get("REMOTE_ADDR")
            if ip and "," in ip:
                ip = ip.split(",")[0]

        if not ip:
            return Response({"error": "IP address required"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate IP format
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            return Response({"error": "Invalid IP address format"}, status=status.HTTP_400_BAD_REQUEST)

        # Get APIKey from authentication
        api_key = request.auth

        # Initialize usage_reset_date if missing
        if not api_key.usage_reset_date:
            api_key.usage_reset_date = timezone.now().date()
            api_key.monthly_usage = 0
            api_key.save()

        # Reset monthly usage every 30 days
        if (timezone.now().date() - api_key.usage_reset_date).days >= 30:
            api_key.monthly_usage = 0
            api_key.usage_reset_date = timezone.now().date()
            api_key.save()

        # GeoIP lookup
        try:
            reader = geoip2.database.Reader(f"{settings.GEOIP_PATH}/GeoLite2-City.mmdb")
            response = reader.city(ip)
            country = response.country.name or "Unknown"
            city = response.city.name or "Unknown"
            latitude = response.location.latitude or 0.0
            longitude = response.location.longitude or 0.0
            isp = getattr(response.traits, "isp", None)
        except Exception:
            return Response({"error": "Unable to lookup IP address"}, status=status.HTTP_400_BAD_REQUEST)

        # Risk logic
        risk_score = 0
        if isp and "hosting" in isp.lower():
            risk_score += 20

        # Increment usage
        api_key.monthly_usage += 1
        api_key.save()

        # Stripe usage tracking for paid tier
        if api_key.monthly_usage > 1000 and getattr(api_key, "stripe_subscription_item_id", None):
            try:
                record_usage(api_key.stripe_subscription_item_id)
            except Exception:
                pass

        # Build response
        result = {
            "ip": ip,
            "country": country,
            "city": city,
            "latitude": latitude,
            "longitude": longitude,
            "isp": isp,
            "risk_score": risk_score,
            "monthly_usage": api_key.monthly_usage,
            "free_requests_remaining": max(0, 1000 - api_key.monthly_usage)
        }

        return Response(result, status=status.HTTP_200_OK)
