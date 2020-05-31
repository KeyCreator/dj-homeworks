from django.conf import settings

from .models import TableField, FilePath


def get_columns():
    fields = TableField.objects.all().order_by('serial')
    return list(fields)


def get_csv_filename():
    FilePath.objects.all().delete()
    csv_filename = FilePath()
    csv_filename.set_path(settings.CSV_FILENAME)
    csv_filename.save()
    return csv_filename.get_path()