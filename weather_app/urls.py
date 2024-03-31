# weather_api_project/urls.py
from django.urls import path
from .import views



urlpatterns = [
    # path('api', views.weather_data_list, name='weather-data-list'),
    # path('Weather', views.Weather, name='Weather'),
    # path('Data', views.WeatherDataShow, name='WeatherDataShow'),
    path('api/', views.fetch_data_view, name='metoffice_data'),
   
  
    

]
