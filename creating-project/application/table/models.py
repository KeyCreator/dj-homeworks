from django.db import models

# Create your models here.

class TableField(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя столбца', blank=False, null=False)
    width = models.IntegerField(default=5, verbose_name='Ширина столбца', blank=False, null=False)
    serial = models.IntegerField(default=10, verbose_name='Порядковый номер', blank=False, null=False)

    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблица'

    def __str__(self):
        return f'{self.serial}: {self.name} ({self.width})'

class FilePath(models.Model):
    path = models.CharField(max_length=512, verbose_name='Путь к csv-файлу', blank=False, null=False)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path

    class Meta:
        verbose_name = 'Путь к csv-файлу'
        verbose_name_plural = 'Путь к csv-файлу'

    def __str__(self):
        return self.path