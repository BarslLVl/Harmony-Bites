from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Booking

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def opentime(request):
    return render(request, 'opentime.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'user_login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def booking(request):
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        user = request.user

        # Create a new booking instance and save it to the database
        booking = Booking(user=user, table_number=1, date=date, time=time, number_of_people=people)
        booking.save()

        messages.success(request, 'Your table has been booked successfully!')
        return redirect('index')

    return render(request, 'booking.html')
