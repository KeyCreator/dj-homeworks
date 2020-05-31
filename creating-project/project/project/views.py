from django.shortcuts import render

from .models import Station, Route

def route_view(request):
    template = 'stations.html'

    context = {
        'routes': Route.objects.all().only('name').order_by('name')
    }

    return render(request, template, context)

def station_view(request):
    template = 'stations.html'

    route = request.GET.get('route')
    route = route[1:]
    stations = list(map(lambda item: {'latitude': item.latitude,
                                      'longitude': item.longitude,
                                      'route_numbers': item.routes,
                                      'name': item.name},
                        Station.objects.filter(routes__name=route).prefetch_related('routes')))

    context = {
        'stations': stations,
        'routes': Route.objects.all().only('name').order_by('name')
    }

    print(stations)
    return render(request, template, context)