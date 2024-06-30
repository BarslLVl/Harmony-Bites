from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book_table/', views.book_table, name='book_table'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('contactus/', views.contactus, name='contactus'),
    path('open_time/', views.open_time, name='open_time'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('admin/delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('admin/edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('admin/delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]
