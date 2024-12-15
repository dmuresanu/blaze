from django.urls import path
from django.views.generic import TemplateView  # Import TemplateView only if needed

urlpatterns = [
    # Example of a booking app route (add your real routes here)
    path('', TemplateView.as_view(template_name='booking_home.html'), name='booking_home'),
    
    # Add any specific booking-related views here
    # e.g., path('reserve/', views.reserve, name='reserve'),
]

