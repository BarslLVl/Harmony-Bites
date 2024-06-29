from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('book_table/', views.book_table, name='book_table'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('about/', views.about, name='about'),
]
