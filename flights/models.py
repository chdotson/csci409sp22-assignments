from django.db import models

# Import the Airport model specifically
from airports.models import Airport

# Create your models here.

class Airline(models.Model):
    airline_name = models.CharField(max_length=255)
    airline_code = models.CharField(max_length=2)

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='flight_origin')
    destination = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='flight_destination')
    departure = models.DateField()
    arrival = models.DateField()
    aircraft_type = models.CharField(max_length=10)
    flight_number = models.IntegerField()
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT)
