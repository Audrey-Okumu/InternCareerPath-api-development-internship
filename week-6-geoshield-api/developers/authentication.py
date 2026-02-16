from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import APIKey
from billing.models import UsageRecord

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None 

        try:
            prefix, key = auth_header.split(" ")
        except ValueError:
            raise AuthenticationFailed("Invalid Authorization header format")

        if prefix != "Bearer":
            raise AuthenticationFailed("Invalid token prefix")

        try:
            api_key = APIKey.objects.get(key=key, active=True)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed("Invalid API key")

        # Increment usage locally
        api_key.monthly_usage += 1
        api_key.save()

        # Record usage
        UsageRecord.objects.create(
            api_key=api_key,
            endpoint=request.path
        )

        # Return (user, auth) tuple as DRF expects
        return (api_key.user, api_key)
