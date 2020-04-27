from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'email', 'phone']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'phone']
    prepopulated_fields = {'username': ('email',)}


admin.site.register(User, UserAdmin)
