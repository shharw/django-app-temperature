from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sensors_location'),
    path('sensor_details/', views.sensor_details, name='sensor_details'),
    path('secure/', views.secure, name='secure'),
    path('api/sensors', views.get_sensors),
    path('api/sensor', views.get_sensor),
    path('api/temperature', views.get_temperature),
    path('api/csv', views.post_csv),
    path('api/temperature_station', views.post_temperature_station),
]