# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from UserLogin.models import UserProfile

# addPlant signifies creating a plant which is linked to a particular User
class Plant(models.Model):
    name = models.CharField(max_length=100)
    plant_id = models.AutoField(primary_key=True)
    Latitude = models.FloatField(null=True)
    Longitude = models.FloatField(null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' Plant: ' + str(self.plant_id) + ' Lat: ' + str(self.Latitude) + ' Long: ' + str(self.Longitude)

class MicroSensor(models.Model):
    micro_id = models.AutoField(primary_key=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,null=True)
    SoilMoisture = models.FloatField(null = True)

    def __str__(self):
        return 'SoilMoisture ' + str(self.SoilMoisture) + " " +str(self.plant)

class MacroSensor(models.Model):
    macro_id = models.AutoField(primary_key=True)
    read_time = models.DateField(auto_now=True)
    Temperature = models.FloatField(null = True)
    Humidity = models.FloatField(null = True)
    WaterLevel = models.FloatField(null=True)
    Rain = models.FloatField(null = True)
    Latitude = models.FloatField(null=True)
    Longitude = models.FloatField(null=True)

    def __str__(self):
        return 'Temperature ' + str(self.Temperature) + 'C - Humidity' + str(self.Humidity) + '% - WaterLevel' + str(self.WaterLevel) + 'cm' + ' Rain ' + str(self.Rain) +'cm'
