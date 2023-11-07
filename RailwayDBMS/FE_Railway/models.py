from django.conf import settings
from django.db import models


class RailwaySystem(models.Model):
    RailwaySystem_id = models.AutoField(primary_key=True)
    RailwaySystem_name = models.CharField(max_length=255)
    RailwaySystem_address = models.CharField(max_length=255)
    RailwaySystem_phone_number = models.CharField(max_length=255)
    RailwaySystem_website = models.CharField(max_length=255)
    
    def __str__(self):
        return self.RailwaySystem_name


class Railway(models.Model):
    Railway_id = models.AutoField(primary_key=True)
    Railway_name = models.CharField(max_length=255)
    Railway_website = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Railway_name


class Train(models.Model):
    train_id = models.AutoField(primary_key=True)
    train_number = models.CharField(max_length=255)
    Railway = models.ForeignKey(Railway, on_delete=models.CASCADE)
    departure_RailwaySystem = models.ForeignKey(RailwaySystem, on_delete=models.CASCADE, related_name='departures')
    arrival_RailwaySystem = models.ForeignKey(RailwaySystem, on_delete=models.CASCADE, related_name='arrivals')
    departure_date = models.DateField()
    arrival_date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    train_status = models.CharField(max_length=255)
    
    def __str__(self):
        return self.train_number
