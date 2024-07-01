from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import SignUpForm, UserEditForm, BookingForm
from .models import Booking

class AdminLoginView(LoginView):
    template_name = 'registration/admin_login.html'

def index(request):
    return render(request, 'bookings/index.html')

@login_required
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful.')
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_table.html', {'form': form})

def booking_success(request):
    return render(request, 'bookings/booking_success.html')

def about(request):
    return render(request, 'bookings/about.html')

def menu(request):
    return render(request, 'bookings/menu.html')

def contactus(request):
    return render(request, 'bookings/contactus.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def admin_dashboard(request):
    bookings = Booking.objects.all()
    return render(request, 'admin_dashboard.html', {'bookings': bookings})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def profile_settings(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'accounts/profile_settings.html', {'form': form})

@login_required
def profile_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'accounts/profile_bookings.html', {'bookings': bookings})

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking cancelled successfully.')
        return redirect('profile_bookings')
    return render(request, 'accounts/delete_booking.html', {'booking': booking})

def open_time(request):
    return render(request, 'bookings/open_time.html')
