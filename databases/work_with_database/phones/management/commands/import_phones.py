import csv
import os

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        path = os.path.join('..', 'phones.csv')
        with open(path, 'r') as csvfile:

            phone_reader = csv.DictReader(csvfile, delimiter=';')

            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                phone = Phone()
                phone.id = line['id']
                phone.name = line['name']
                phone.image = line['image']
                phone.price = line['price']
                phone.release_date = line['release_date']
                print(f'PRICE IS {phone.release_date}')
                print(f'LTE IS {line["lte_exists"]}, {type(line["lte_exists"])}')
                phone.lte_exists = line['lte_exists']
                phone.slug = slugify(phone.name)
                phone.save()
