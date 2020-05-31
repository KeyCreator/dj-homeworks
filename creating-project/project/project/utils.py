from .models import Station, Route


def get_routes():
    routes = Route.objects.all().only('name').order_by('name')
    routes = map(lambda route: route.name, routes)
    return list(routes)


def get_stations(route):
    stations = Station.objects.filter(routes=route).prefetch_related('routes')

    stations = map(lambda station: {'latitude': station.latitude,
                                 'longitude': station.longitude,
                                 'route_numbers': route.stations.all(), # TODO: нужно инвертировать связь
                                 'name': station.name},
                   stations)
    return list(stations)