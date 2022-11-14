from rest_framework import serializers
from .models import TemperatureStation

class TemperatureSensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureStation
        fields = ('id', 'sensor_name', 'model_sensor', 'sensor_group')


class TemperatureSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureStation
        fields = '__all__'

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureStation
        fields = ('id', 'temperature')
  