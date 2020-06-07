from django.contrib import admin
from .models import Parking, ParkingSpot


class ParkingAdmin(admin.ModelAdmin):
    list_display = ['cnpj', 'parking_name', 'user', 'full_address', 'price_per_hour', 'amount_parking_spots', 'available_parking_spots']
    search_fields = ['cnpj', 'parking_name', 'user__email', 'full_address', 'price_per_hour']


class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'parking_name', 'parking', 'status', 'driver_name', 'driver']
    search_fields = ['status']


admin.site.register(Parking, ParkingAdmin)
admin.site.register(ParkingSpot, ParkingSpotAdmin)
