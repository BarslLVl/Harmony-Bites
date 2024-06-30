from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm
from .models import Booking

class AdminLoginView(LoginView):
    template_name = 'registration/admin_login.html'

def index(request):
    return render(request, 'bookings/index.html')

@login_required
def book_table(request):
    # Your booking logic here
    return render(request, 'bookings/book_table.html')

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
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def admin_dashboard(request):
    bookings = Booking.objects.all()
    return render(request, 'admin_dashboard.html', {'bookings': bookings})

@login_required
def edit_user(request, user_id):
    # Your edit user logic here
    return render(request, 'admin_dashboard.html')

@login_required
def delete_user(request, user_id):
    # Your delete user logic here
    return render(request, 'admin_dashboard.html')

@login_required
def edit_booking(request, booking_id):
    # Your edit booking logic here
    return render(request, 'admin_dashboard.html')

@login_required
def delete_booking(request, booking_id):
    # Your delete booking logic here
    return render(request, 'admin_dashboard.html')

def open_time(request):
    return render(request, 'bookings/open_time.html')
