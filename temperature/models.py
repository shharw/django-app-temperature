from django.db import models

class TemperatureStation(models.Model):
    sensor_location = models.CharField(max_length=22)
    measurement_date = models.DateField() 
    measurement_time = models.TimeField()
    temperature = models.IntegerField()
    sensor_name = models.TextField()
    model_sensor = models.TextField()
    sensor_group = models.TextField()    