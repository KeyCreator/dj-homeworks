from django.core.cache import cache

from .models import City

def get_cities():
    cache_key = 'cities:cities-list'
    cities = cache.get(cache_key)
    if not cities:
        cities = City.objects.all().only('name').order_by('name')
        cache.set(cache_key, cities, timeout=60)
    return cities
