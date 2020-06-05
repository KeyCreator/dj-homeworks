from django.contrib import admin

from .models import Station, Route, StationRoute

class StationRouteInline(admin.TabularInline):
    model = Station.routes.through

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    inlines = (StationRouteInline,)
    ordering = ('name',)

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    ordering = ('name', )


