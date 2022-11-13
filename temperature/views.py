from django.http import HttpResponse
from django.template import loader
from .models import TemperatureStation

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
