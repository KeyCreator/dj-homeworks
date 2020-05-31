from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return self.name


class Station(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    routes = models.ManyToManyField(Route, related_name='stations')
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Автобусная остановка'
        verbose_name_plural = 'Автобусные остановки'

    def __str__(self):
        return self.name