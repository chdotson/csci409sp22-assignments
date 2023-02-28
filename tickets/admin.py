from django.contrib import admin
from .models import Reservation, Tickets

# Register your models here.
class TicketsInLine(admin.StackedInline):
    model = Tickets  # Specify which model to use
    extra = 2       # How many to start with

class ReservationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['flight', 'num_people', 'total_cost']})
    ]
    inlines = [TicketsInLine]  # Load the class

admin.site.register(Reservation, ReservationAdmin)