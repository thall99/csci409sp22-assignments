from django.contrib import admin
from .models import Ticket, Reservation


# Register your models here.
class TicketsInline(admin.StackedInline):
    model = Ticket
    extra = 2


class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    inlines = [TicketsInline]


admin.site.register(Reservation, ReservationAdmin)
