from django.http import HttpResponse
from .models import Flight # Import Flight model
from airports.models import Airport # Import airport model to get airport id and code
from django.shortcuts import render
from .models import Flight
from .forms import FlightForm

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    # Create instance
    form = FlightForm()
    # Render the form
    return render(request, 'flights/index.html', {'form': form})

    # Fetch all flights
    # flights = Flight.objects.all()
    # flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code for f in flights])
    # return HttpResponse('Listing all flights: ' + flight_list)

@login_required
def flight_search(request, origin, destination):
    origin = Airport.objects.get(airport_code=origin)
    destination = Airport.objects.get(airport_code=destination)
    # Code to select flights from the database
    flights = Flight.objects.all()
    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " +
                             f.airline.airline_code for f in flights])
    return HttpResponse('Showing flights: ' + flight_list)

def search(request):
    form = FlightForm(request.POST)
    if form.is_valid():
        # takeoff1 = Airport.objects.get(airport_code=form.cleaned_data['from_origin'])
        # landing1 = Airport.objects.get(airport_code=form.cleaned_data['to_destination'])
        # Then
        takeoff = Flight.objects.get(origin=form.cleaned_data['from_origin'],
                                     destination=form.cleaned_data['to_destination'])
        # landing = Flight.objects.get(destination=form.cleaned_data['to_destination'])
        # Finally
        return render(request, 'flights/flight_search.html', {'takeoff': takeoff}) #, 'landing': landing})

    # flight = Airport.objects.get(airport_code=form.cleaned_data['from_origin'])
    # return render(request, 'flights/flight_search.html', {'flight': flight})

