from django.http import HttpResponse
from .models import Airport

# Create your views here.
# Clark Dotson - CSCI409-D1

def index(request):
    # Fetch all airports from database
    airports = Airport.objects.all()
    # Create a displayable string. We will change next week.
    # This is just to show data
    airport_list = ', '.join([a.airport_code for a in airports])
    return HttpResponse('Showing all airports: ' + airport_list);

def airport_info(request, airport_code):
    #
    #
    airport = Airport.objects.get(airport_code=airport_code)
    #
    return HttpResponse('Showing info for airport: ' + airport.name + "- " + airport.airport_code);
