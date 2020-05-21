from django import forms

from .widgets import AjaxInputWidget
from .models import Ticket, City


class SearchTicket(forms.Form):
    # Добавьте здесь поля, описанные в задании
    departure_city = forms.CharField(widget=AjaxInputWidget(url='api/city_ajax', attrs={'class': 'inline right-margin'}),
                                     label='Город вылета')

    cities = City.objects.all().only('name').order_by('name')
    cities = list(map(lambda city: (city.id, city.name), cities))
    print(cities)
    arrival_city = forms.ChoiceField(widget=forms.Select, choices=cities, label='Город прилета')
    departure_date = forms.DateField(widget=forms.SelectDateWidget(), label='Дата')

    class Meta:
        model = Ticket
        fields = ['departure_city', 'arrival_city', 'departure_date']
