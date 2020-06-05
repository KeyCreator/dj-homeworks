import csv
import os

from django.core.management.base import BaseCommand

from project.models import Station, Route, StationRoute
from project.utils import get_routes_set


# https://django.fun/tutorials/sozdanie-polzovatelskih-komand-upravleniya-v-django/
class Command(BaseCommand):
    help = u'Создание случайного пользователя'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help=u'Загружаемый файл с данными')

    def handle(self, *args, **kwargs):
        print('Текущая папка', os.getcwd())
        print('Данные загружаются')
        path = kwargs['path']
        with open(path, 'r') as csvfile:

            station_reader = csv.DictReader(csvfile, delimiter=';')
            station_reader = list(station_reader)

            Station.objects.all().delete()
            Route.objects.all().delete()
            StationRoute.objects.all().delete()

            routes = get_routes_set(station_reader)
            Route.objects.bulk_create([Route(name=item) for item in routes])

            stations = [Station(uid=item['ID'],
                                name=item['Name'],
                                longitude=item['Longitude_WGS84'],
                                latitude=item['Latitude_WGS84'])
                        for item in station_reader]
            Station.objects.bulk_create(stations)

            # получаем словарь станций, ключ - uid
            station_objects = {s.uid: s for s in Station.objects.all()}

            # получаем словарь маршрутов, ключ - name
            route_objects = {item.name.strip(): item for item in Route.objects.all()}

            station_route = list()
            for i, item in enumerate(station_reader):
                foo = [StationRoute(station=station_objects.get(int(item['ID'])),
                                    route=route_objects.get(bar))
                       for bar in map(lambda x: x.strip(), item['RouteNumbers'].split(';'))]
                station_route += foo
                if not i % 100:
                    print('.', end='', flush=True)
            StationRoute.objects.bulk_create(station_route)

            # station_route = list()
            # for i, item in enumerate(station_reader):
            #     foo = [StationRoute(station=Station.objects.get(uid=item['ID']),
            #                         route=bar)
            #            for bar in Route.objects.filter(name__in=item["RouteNumbers"].split(';'))]
            #     station_route += foo
            #     if not i % 100:
            #         print('.', end='', flush=True)
            # StationRoute.objects.bulk_create(station_route)


        print('\nДанные успешно загружены')