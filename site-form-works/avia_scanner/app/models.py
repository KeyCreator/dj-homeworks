from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'

class Ticket(models.Model):
    departure_city = models.ForeignKey(City,
                                       verbose_name='Город отправления',
                                       on_delete=models.DO_NOTHING,
                                       related_name='departure_city')
    arrival_city = models.ForeignKey(City,
                                     verbose_name='Город прибытия',
                                     on_delete=models.DO_NOTHING,
                                     related_name='arrival_city')
    departure_date = models.DateField(verbose_name='Дата', null=False, blank=False)

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        return f'{self.departure_date}: {self.departure_city} - {self.departure_date}'