from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sensors_location'),
    path('sensor_details/', views.sensor_details, name='sensor_details'),
    path('secure/', views.secure, name='secure'),
]