from django.contrib import admin
from .models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Status)
