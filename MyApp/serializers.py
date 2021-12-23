from rest_framework import serializers
from rest_framework.exceptions import server_error

class HelloSerializer(serializers.Serializer):
    """Serializer a name filed for testing our APIView"""

    name = serializers.CharField(max_length=10)
    