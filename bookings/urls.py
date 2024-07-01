from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.index, name='home'),
    path('book_table/', views.book_table, name='book_table'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('contactus/', views.contactus, name='contactus'),
    path('signup/', views.signup, name='signup'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('profile/', views.profile, name='profile'),
    path('profile/settings/', views.profile_settings, name='profile_settings'),
    path('profile/bookings/', views.profile_bookings, name='profile_bookings'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('open_time/', views.open_time, name='open_time'),
]
