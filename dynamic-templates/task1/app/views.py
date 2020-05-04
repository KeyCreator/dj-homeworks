from django.shortcuts import render
import csv
from pprint import pprint

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', delimetr=';') as csvfile:
        reader = csv.DictReader(csvfile)
        # stations = map(lambda item: {'Year': item['Год'],'Street': item['Street'], 'District': item['District']}, reader)
        # stations = list(stations)

    pprint(reader)
    context = {}

    return render(request, template_name,
                  context)