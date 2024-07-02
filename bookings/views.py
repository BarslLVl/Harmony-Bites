from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import SignUpForm, UserEditForm, BookingForm, AdminUserEditForm
from .models import Booking, User

class AdminLoginView(LoginView):
    template_name = 'registration/admin_login.html'

class UserLoginView(LoginView):
    template_name = 'registration/login.html'

def index(request):
    return render(request, 'bookings/index.html')

def custom_page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)

@login_required
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successfully created.')
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

def opening_times(request):
    return render(request, 'bookings/opentimes.html')

def contactus(request):
    return render(request, 'bookings/contactus.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

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
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking cancelled successfully.')
        return redirect('profile_bookings')
    return render(request, 'admin/confirm_delete.html', {'object': booking})

@login_required
def edit_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('profile_bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'admin/edit_booking.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    users = User.objects.all()
    bookings = Booking.objects.all()
    return render(request, 'admin/admin_dashboard.html', {'users': users, 'bookings': bookings})

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    users = User.objects.all()
    return render(request, 'admin/users.html', {'users': users})

@user_passes_test(lambda u: u.is_superuser)
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = AdminUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('admin_users')
    else:
        form = AdminUserEditForm(instance=user)
    return render(request, 'admin/edit_user.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('admin_users')
    return render(request, 'admin/confirm_delete.html', {'object': user})
