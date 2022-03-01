from django.contrib import admin
from .models import Airline, Flight

class AirlineAdmin(admin.ModelAdmin):
    model = Airline

class FlightAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Airline Information', {
            'fields': ('airline', 'flight_number')
        }),
        ('Origin / Destination', {
            'fields': ('origin', 'destination'),
        }),
        ('Departure and Arrival Time', {
            'classes': ('collapse',),
            'fields': ('departure', 'arrival'),
        }),
    )

admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)

