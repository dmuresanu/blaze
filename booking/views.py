# booking/views.py

from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # Import login_required decorator

# Create your views here.

@login_required  # This ensures only logged-in users can access this view
def booking_form(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking confirmed!")
            return redirect('confirmation')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})

def confirmation(request):
    return render(request, 'booking/confirmation.html')

