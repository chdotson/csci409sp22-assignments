from django.shortcuts import render

# Create your views here.
# Clark Dotson - CSCI409-D1

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello from flights');

def flight_search(request, origin, destination):
    return HttpResponse('Showing flights from ' + origin + ' to ' + destination);

