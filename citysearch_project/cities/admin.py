from django.contrib import admin

from .models import Flightroute

class FlightrouteAdmin(admin.ModelAdmin):
    list_display = ("month", "count", "origin_city", "destination_city")

admin.site.register(Flightroute, FlightrouteAdmin)