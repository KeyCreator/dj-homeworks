from django.shortcuts import render

from .models import Station, Route
from .utils import get_routes, get_stations

def route_view(request):
    template = 'stations.html'

    context = {
        'routes': get_routes()
    }

    return render(request, template, context)

def station_view(request):
    template = 'stations.html'

    route_name = request.GET.get('route')
    route_name = route_name[1:]
    route = Route.objects.get(name=route_name)

    context = {
        'stations': get_stations(route),
        'routes': get_routes()
    }

    print(context['stations'])

    return render(request, template, context)