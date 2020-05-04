from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv
from urllib.parse import urlencode


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):

    with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = map(lambda item: {'Name': item['Name'], 'Street': item['Street'], 'District': item['District']},
                           reader)
        stations = list(stations)

    paginator = Paginator(stations, 10)
    current_page = request.GET.get('page', 1)
    station_objs = paginator.get_page(current_page)
    # return render(request, 'index.html', {'bus_stations': station_objs})
    prev_page, next_page = None, None
    if station_objs.has_previous():
        prev_page = station_objs.previous_page_number()
        prev_page = '?%s' % urlencode({'page': prev_page})
    if station_objs.has_next():
        next_page = station_objs.next_page_number()
        next_page = '?%s' % urlencode({'page': next_page})

    return render(request, 'index.html', context={
        'bus_stations': station_objs,
        'current_page': current_page,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    })

