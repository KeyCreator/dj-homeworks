from django.shortcuts import render
from phones.management.commands.import_phones import Command
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    sort_field = request.GET.get('sort')
    if sort_field == 'name':
        phones = Phone.objects.order_by('name')
    elif sort_field == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif sort_field == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.all()

    print(list(phones))   # Строчка debug'а
    for phone in phones:
        print(phone)
    context = {'phones': list(phones)}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    print('показываем карточку', phone)
    context = {'phone': phone}
    return render(request, template, context)
