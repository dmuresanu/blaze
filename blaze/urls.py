"""
URL configuration for blaze project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # For rendering a static homepage

urlpatterns = [
    # Admin page
    path('admin/', admin.site.urls),
    
    # Homepage route
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Default home page

    # Profiles app URLs
    path('profiles/', include('profiles.urls')),  # Link Profiles app with a 'profiles' prefix

    # Booking app URLs
    path('booking/', include('booking.urls')),  # Link Booking app with a 'booking' prefix
]
