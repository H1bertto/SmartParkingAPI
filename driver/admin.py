from django.contrib import admin
from .models import Driver, Vehicle


class DriverAdmin(admin.ModelAdmin):
    list_display = ['user', 'cpf', 'latitude', 'longitude']
    search_fields = ['cpf', 'latitude', 'longitude']


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['plate', 'driver', 'type', 'brand', 'vehicle_model', 'color']
    search_fields = ['plate', 'driver__user__email', 'type', 'brand', 'vehicle_model', 'color']


admin.site.register(Driver, DriverAdmin)
admin.site.register(Vehicle, VehicleAdmin)
