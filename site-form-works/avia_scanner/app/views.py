import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket
from .utils import get_cities


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    pattern = request.GET.get('term')
    if pattern:
        pattern = pattern.lower().capitalize()

    cities = get_cities()
    cities = map(lambda city: city.name, cities)
    cities = filter(lambda city: city.startswith(pattern), cities)
    # cities = cities.filter(name__startswith=pattern)
    cities = list(cities)
    print('Выборка для виджета', cities)
    return JsonResponse(cities, safe=False)
