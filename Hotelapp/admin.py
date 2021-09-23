from django.contrib import admin
from .models import Hotel


class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'opening_hour']


admin.site.register(Hotel, HotelAdmin)
