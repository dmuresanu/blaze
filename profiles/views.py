from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .models import Profile
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'profiles/register.html', {'form': form})

# Profile view
@login_required
def profile(request):
    return render(request, 'profiles/profile.html')

# Update Profile view
@login_required
def update_profile(request):
    return render(request, 'profiles/update_profile.html')

# Delete Profile view
@login_required
def delete_profile(request):
    return render(request, 'profiles/delete_profile.html')    

def test_view(request):
    return HttpResponse("This is a test view!")


