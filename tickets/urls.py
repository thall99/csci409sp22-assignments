from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index),
    path('/<str:confirmation_number>', views.ticket_search),
    path('/search/',views.search),
]
