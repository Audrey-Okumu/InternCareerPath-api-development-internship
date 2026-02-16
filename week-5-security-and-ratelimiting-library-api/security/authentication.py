from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import APIKey

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        key = request.headers.get("X-API-KEY")

        if not key:
            return None  # allow JWT later

        if not APIKey.objects.filter(key=key, is_active=True).exists():
            raise AuthenticationFailed("Invalid API Key")

        return (None, None)
