from rest_framework import serializers

class IPAnalyzeSerializer(serializers.Serializer):
    ip = serializers.IPAddressField(required=False)
