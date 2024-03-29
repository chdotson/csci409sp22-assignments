# Load a path from django.urls
from django.urls import path
# Load this app's views.py file
from . import views

# Define url patterns
urlpatterns = [
    # Get the index value
    # Example url: /airports/
    path('/', views.index),
    # Show Info
    # Example url: /airports/MYR
    # NOTICE: the airport_code param in the url matches
    # the param in the airport_info func
    path('/<int:confirmation_number>', views.ticket_search),
    # New route added
    path('/search/', views.search),
]
