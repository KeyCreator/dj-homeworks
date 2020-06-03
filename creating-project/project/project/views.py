from django.shortcuts import render

from .models import Station, Route
from .utils import get_routes, get_stations, get_center

def route_view(request):
    template = 'stations.html'

    context = {
        'routes': get_routes()
    }

    return render(request, template, context)

def station_view(request):
    template = 'stations.html'

    route_name = request.GET.get('route')
    print(route_name, len(route_name))
    route = Route.objects.get(name=route_name)

    stations = get_stations(route)
    x, y = get_center(stations)
    center = {'x': x, 'y': y}

    context = {
        'stations': stations,
        'routes': get_routes(),
        'center': center
    }

    print(context['stations'], context['center'])

    return render(request, template, context)