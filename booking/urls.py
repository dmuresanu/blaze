# booking/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('some_booking_page/', views.booking_form, name='booking_form'),  # Corrected view name
    path('confirmation/', views.confirmation, name='confirmation'),       # Confirmation page
]

