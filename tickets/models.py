from django.db import models

# Import the Flight model specifically
from flights.models import Flight

# Create your models here.

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    num_people = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

class Tickets(models.Model):
    # Choice Designation
    FIRST_CLASS = 'F'
    BUSINESS_CLASS = 'B'
    MAIN_CABIN = 'M'
    TICKET_TYPE_CHOICES = [
        (FIRST_CLASS, 'First Class'),
        (BUSINESS_CLASS, 'Business Class'),
        (MAIN_CABIN, 'Main Cabin'),
    ]
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT)
    seat = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_class = models.CharField(max_length=1, choices=TICKET_TYPE_CHOICES, default=MAIN_CABIN)

