from functools import reduce

from .models import Station, StationRoute, Route


def get_routes(station=None):
    if not station:
        routes = Route.objects.all().order_by('name').values_list('name')
    else:
        routes = station.routes.all().order_by('name').values_list('name')
    routes = map(lambda item: item[0].strip(), routes)
    return list(routes)


def get_stations(route):
    stations = Station.objects.filter(routes=route).prefetch_related('routes')

    stations = map(lambda station: {'latitude': station.latitude,
                                    'longitude': station.longitude,
                                    'route_numbers': get_routes(station=station),
                                    'name': station.name},
                   stations)
    return list(stations)

def get_center(stations):
    x = (stations[0]['longitude'] + stations[-1]['longitude']) / 2
    y = (stations[0]['latitude'] + stations[-1]['latitude']) / 2

    return x, y

def get_routes_set(station_reader):
    get_list = lambda s: reduce(lambda d, el: d.extend(el) or d, s, [])

    routes = map(lambda item: item["RouteNumbers"].replace(' ', '').split(';'), station_reader)
    routes = get_list(routes)
    routes = set(routes)

    return routes