# weather_api/serializers.py
from rest_framework import serializers
# from .models import WeatherData

# class WeatherDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WeatherData
#         fields = '__all__'

from rest_framework import serializers

class MetOfficeDataSerializer(serializers.Serializer):
    data = serializers.CharField()