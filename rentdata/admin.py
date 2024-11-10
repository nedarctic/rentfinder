from django.contrib import admin

from .models import RentData, Apartment

admin.site.register(RentData)
admin.site.register(Apartment)