from django.http import HttpResponse
from .models import Reservation

def index(request):
    # Nothing to do here
    tickets = Reservation.objects.all()
    return HttpResponse('Showing all airports: ' + tickets);

def ticket_search(request, confirmation_number):
  return HttpResponse('Search for tickets for confirmation number: ' + confirmation_number)
    # Select the singular reservation for the confirmation number
    # Note: the confirmation_number is the id in the Reservation table
    #reservation = Reservation.objects.get(id=confirmation_number)

    #return HttpResponse('Number of tickets for confirmation number: ' + str(confirmation_number) + " is " + str(reservation.num_people))