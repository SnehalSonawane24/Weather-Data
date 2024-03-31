# weather_api/tests.py
from django.test import TestCase
from .models import WeatherData

class WeatherDataModelTestCase(TestCase):
    def test_weather_data_creation(self):
        WeatherData.objects.create(year=2025, jan=7.3, feb=9.0, mar=8.9, apr=11.1, may=16.2, jun=16.5, jul=21.2, aug=19.3, sep=19.4, oct=14.0, nov=9.3, dec=8.3, winter_mean=7.34, spring_mean=12.38, summer_mean=19.74, autumn_mean=14.22, annual_mean=13.66)
        self.assertEqual(WeatherData.objects.count(), 1)
