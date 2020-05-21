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
    cities = map(lambda city: (city.id, city.name), cities)
    cities = filter(lambda city: city[1].startswith(pattern), cities)
    # cities = cities.filter(name__startswith=pattern)

    print('Выборка для виджета', list(cities))
    return JsonResponse(list(cities), safe=False)
