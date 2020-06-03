import csv
import os

from django.core.management.base import BaseCommand

from project.models import Station, Route
from project.utils import get_routes_set


# https://django.fun/tutorials/sozdanie-polzovatelskih-komand-upravleniya-v-django/
class Command(BaseCommand):
    help = u'Создание случайного пользователя'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help=u'Загружаемый файл с данными')

    def handle(self, *args, **kwargs):
        print('Текущая папка', os.getcwd())
        print('Данные загружаются ...')
        path = kwargs['path']
        with open(path, 'r') as csvfile:

            station_reader = csv.DictReader(csvfile, delimiter=';')
            station_reader = list(station_reader)

            Station.objects.all().delete()
            Route.objects.all().delete()

            routes = get_routes_set(station_reader)
            Route.objects.bulk_create([Route(name=item) for item in routes])

            stations = [Station(name=item['Name'],
                                longitude=item['Longitude_WGS84'],
                                latitude=item['Latitude_WGS84'])
                        for item in station_reader]
            Station.objects.bulk_create(stations)

            for station, line in zip(Station.objects.all(), station_reader):
                routes = Route.objects.filter(name__in=line["RouteNumbers"].split(';'))
                station.routes.set(routes)

        print('Данные успешно загружены')