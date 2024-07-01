from django.urls import path
from .views import (
    index, about, menu, contactus, signup, book_table, booking_success,
    profile, profile_settings, profile_bookings, delete_booking, edit_booking,
    admin_dashboard, admin_users, edit_user, delete_user, AdminLoginView, UserLoginView
)
from django.contrib.auth.views import LogoutView, PasswordResetView
from django.urls import reverse_lazy

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('contactus/', contactus, name='contactus'),
    path('signup/', signup, name='signup'),
    path('book_table/', book_table, name='book_table'),
    path('booking_success/', booking_success, name='booking_success'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/settings/', profile_settings, name='profile_settings'),
    path('accounts/profile/bookings/', profile_bookings, name='profile_bookings'),
    path('accounts/profile/bookings/delete/<int:pk>/', delete_booking, name='delete_booking'),
    path('accounts/profile/bookings/edit/<int:pk>/', edit_booking, name='edit_booking'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin/users/', admin_users, name='admin_users'),
    path('admin/users/edit/<int:pk>/', edit_user, name='edit_user'),
    path('admin/users/delete/<int:pk>/', delete_user, name='delete_user'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('admin/login/', AdminLoginView.as_view(), name='admin_login'),
    path('password_reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
]
