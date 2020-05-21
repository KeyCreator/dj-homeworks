from django.contrib import admin

from .models import City, Ticket


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )

class TicketAdmin(admin.ModelAdmin):
    list_display = ('departure_city', 'arrival_city', 'departure_date')

admin.site.register(City, CityAdmin)
admin.site.register(Ticket, TicketAdmin)
