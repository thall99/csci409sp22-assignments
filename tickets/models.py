from django.db import models
from flights.models import Flight
# Create your models here.

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    num_people = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10,decimal_places=2)


class Ticket(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT)
    seat = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    FIRSTCLASS = 'F'
    BUSINESSCLASS = 'B'
    MAINCABIN = 'M'
    class_choices = [
        (FIRSTCLASS, 'First Class'),
        (BUSINESSCLASS, 'Business Class'),
        (MAINCABIN, 'Main Cabin'),
    ]
    ticket_class = models.CharField(max_length=1, choices=class_choices)