from django.shortcuts import render

# Create your views here.
# Clark Dotson - CSCI409-D1

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello from tickets');

def ticket_search(request, confirmation_number):
    return HttpResponse('Search for tickets for Confirmation Number: ' + str(confirmation_number));


