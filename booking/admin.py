from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'check_in', 'check_out', 'parking', 'parking_spot', 'driver', 'total_time', 'total_price', 'its_coming_out']
    search_fields = ['check_in', 'check_out', 'parking__cnpj', 'driver__cpf', 'total_time', 'total_price', 'its_coming_out']


admin.site.register(Booking, BookingAdmin)
