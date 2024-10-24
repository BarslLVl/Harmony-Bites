from django.contrib import admin
from .models import Booking, Table

# Customize the admin interface for the Booking model
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'people')
    search_fields = ('name', 'email')
    list_filter = ('date', 'people')

# Customize the admin interface for the Table model
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity')
    search_fields = ('number',)
# Register your models here.
admin.site.register(Booking)
admin.site.register(Table)