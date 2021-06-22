from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name fils for our Api view"""
    name = serializers.CharField(max_length=10)