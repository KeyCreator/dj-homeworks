from django.db import models


ATTR_LEN = 255


# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=ATTR_LEN)
    price = models.FloatField()
    operating_system = models.CharField(max_length=ATTR_LEN)
    screen_resolution = models.CharField(max_length=ATTR_LEN)
    camera_resolution = models.CharField(max_length=ATTR_LEN)
    ram_amount = models.IntegerField()

    def __str__(self):
        return f'Модель {self.name}, цена {self.price} руб., RAM {self.ram_amount} ГБ'


class Feature(models.Model):
    name = models.CharField(max_length=ATTR_LEN)
    phone = models.ForeignKey(to='Phone', on_delete=models.CASCADE, related_name='phonefeature')

    def __str__(self):
        return f'{self.name} для {self.phone}'
