# Generated by Django 3.0.6 on 2020-05-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_auto_20200530_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablefield',
            name='width',
            field=models.FloatField(default=5, verbose_name='Ширина столбца'),
        ),
    ]