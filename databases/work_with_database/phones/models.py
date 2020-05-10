from typing import Type

from django.db import models
from django.db.models import ImageField

ATTR_LEN=255

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=ATTR_LEN)
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name}, дата выпуска {self.release_date}, поддержка LTE {self.lte_exists}, обозначение {self.slug}'

