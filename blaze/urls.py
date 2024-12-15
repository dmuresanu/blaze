"""
URL configuration for blaze project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # For rendering a static homepage
from django.contrib.auth import views as auth_views  # For login/logout views

urlpatterns = [
    # Admin page
    path('admin/', admin.site.urls),
    
    # Homepage route
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Default home page

    # Profiles app URLs (this is your registration/login system)
    path('profiles/', include('profiles.urls')),  # Link Profiles app with a 'profiles' prefix

    # Authentication URLs (Login, Logout)
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Booking app URLs (Restricted to logged-in users)
    path('booking/', include('booking.urls')),  # Link Booking app with a 'booking' prefix
]
