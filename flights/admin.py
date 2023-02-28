from django.contrib import admin
from .models import Flight, Airline

# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Airline Information', {'fields': ['airline', 'flight_number']}),
        ('Origin/Destination', {'fields': ['origin', 'destination']}),
        ('Departure/Arrival Time', {'fields': ['departure', 'arrival'], 'classes': ['collapse']})
    ]

class AirlineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['airline_name', 'airline_code']})
        ]

admin.site.register(Flight, FlightAdmin)
admin.site.register(Airline, AirlineAdmin)