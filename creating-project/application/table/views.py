import csv

from django.shortcuts import render

from .tools import get_columns, get_csv_filename
from .models import FilePath


# Create your views here.
def table_view(request):
    csv_filename = get_csv_filename()
    template = 'table.html'

    with open(csv_filename, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': get_columns(),
            'table': table,
            'csv_file': csv_filename
        }
        result = render(request, template, context)
    return result