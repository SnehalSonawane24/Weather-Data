
from rest_framework import serializers


from rest_framework import serializers

class MetOfficeDataSerializer(serializers.Serializer):
    data = serializers.CharField()