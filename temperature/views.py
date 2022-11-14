from django.http import HttpResponse
from django.template import loader
from .models import TemperatureStation
from .serializers import TemperatureSerializer, TemperatureSensorSerializer, TemperatureSensorsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage

def index(request):
    sensors = TemperatureStation.objects.all().values()
    context = {
        'sensors': sensors,
    }
    template = loader.get_template('sensors_location.html')
    return HttpResponse(template.render(context, request))

def sensor_details(request):  
    sensors = TemperatureStation.objects.order_by('sensor_location')
    context = {
        'sensors': sensors,        
    }
    template = loader.get_template('sensor_details.html')
    return HttpResponse(template.render(context, request))

def secure(request):  
    template = loader.get_template('secure.html')
    return HttpResponse(template.render({}, request))

@api_view(['GET'])
def get_sensors(request):
    sensors = TemperatureStation.objects.all()
    serializer = TemperatureSensorsSerializer(sensors, many=True)
    return Response(serializer.data)
        

@api_view(['GET'])
def get_sensor(request):
    sensor = TemperatureStation.objects.filter(id=request.query_params['id'])
    serializer = TemperatureSensorSerializer(sensor, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_temperature(request):
    temperature = TemperatureStation.objects.filter(id=request.query_params['id'])
    serializer = TemperatureSerializer(temperature, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_temperature_station(request):
    serializer = TemperatureSensorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def post_csv(request):
    file = request.FILES['csv']
    file_name = default_storage.save(file.name, file)
    resp = {
        file_name: 'saved'
    }
    return Response(resp)