from django.contrib import admin

from .models import Station, Route, StationRoute

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    pass


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    ordering = ('name', )


# @admin.register(Relationship)
# class RouteAdmin(admin.ModelAdmin):
#     pass