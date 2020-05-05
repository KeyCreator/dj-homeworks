from django.shortcuts import render
import csv
from pprint import pprint

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        # stations = map(lambda item: {'Year': item['Год'],'Street': item['Street'], 'District': item['District']}, reader)
        # stations = list(stations)
        years = list(reader)

    print(years)

    context = {'years': years}

    return render(request, template_name,
                  context)