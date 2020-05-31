import csv
import os
from django.core.management.base import BaseCommand

from project.models import Station, Route


# https://django.fun/tutorials/sozdanie-polzovatelskih-komand-upravleniya-v-django/
class Command(BaseCommand):
    help = u'Создание случайного пользователя'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help=u'Загружаемый файл с данными')

    def handle(self, *args, **kwargs):
        print('Текущая папка', os.getcwd())
        path = kwargs['path']
        with open(path, 'r') as csvfile:

            station_reader = csv.DictReader(csvfile, delimiter=';')

            print('Данные загружаются ...')
            Station.objects.all().delete()
            Route.objects.all().delete()

            for line in station_reader:
                # TODO: Добавьте сохранение модели
                station = Station()
                station.id = line['ID']
                station.name = line['Name']
                station.longitude = line["Longitude_WGS84"]
                station.latitude = line["Latitude_WGS84"]
                station.save()

                for name in line["RouteNumbers"].split(';'):
                    if Route.objects.filter(name=name).count():
                        route = Route.objects.get(name=name)
                    else:
                        route = Route.objects.create(name=name)
                    station.routes.add(route)

        print('Данные успешно загружены')