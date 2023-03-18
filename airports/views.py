from django.http import HttpResponse
from django.shortcuts import render  # Library Templates
from .models import Airport

# Create your views here.
# Clark Dotson - CSCI409-D1

def index(request):
    # Fetch all airports from database
    airports = Airport.objects.all()
    #
    context = {'airports': airports}
    return render(request, 'airports/index.html', context)

    # airport_list = ', '.join([a.airport_code for a in airports])
    # return HttpResponse('Showing all airports: ' + airport_list);

def airport_info(request, airport_code):
    #
    #
    airports = Airport.objects.get(airport_code=airport_code)
    #
    context = {'airports': airports}
    return render(request, 'airports/airport.html', context)

    # airport = Airport.objects.get(airport_code=airport_code)
    #
    # return HttpResponse('Showing info for airport: ' + airport.name + "- " + airport.airport_code);
