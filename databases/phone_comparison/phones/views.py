from django.shortcuts import render
from phones.models import Phone, Feature


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    for phone in phones:
        print(phone.__dict__)
    context = {'phones': list(phones)}
    return render(
        request,
        template,
        context
    )
