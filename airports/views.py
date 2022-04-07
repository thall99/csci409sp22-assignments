from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Airport

def index(request):
    airports = Airport.objects.all()
    context = {'airports': airports}
    return render(request, 'airports/index.html', context)



def airport_info(request, airport_code):
    airport = Airport.objects.get(airport_code=airport_code)
    context = {'airport': airport}
    return render(request, 'airports/airport.html', context)

