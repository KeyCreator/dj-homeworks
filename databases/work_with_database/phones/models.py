from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField
    name = models.TextField
    price = models.FloatField
    image = models.TextField
    release_date = models.DateField
    lte_exist = models.BooleanField
    slug = models.SlugField

