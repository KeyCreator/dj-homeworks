# Generated by Django 3.0.6 on 2020-05-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablefield',
            name='serial',
            field=models.IntegerField(default=10, verbose_name='Порядковый номер'),
        ),
    ]