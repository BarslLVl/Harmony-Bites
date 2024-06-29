from django.contrib import admin
from django.urls import path, include
from bookings import views as bookings_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')),
    path('', bookings_views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin-login/', bookings_views.admin_login_view, name='admin_login'),
    path('admin-dashboard/', bookings_views.admin_dashboard, name='admin_dashboard'),
]
