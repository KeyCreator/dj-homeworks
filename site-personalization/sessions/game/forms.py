from django import forms
from .models import Player, Game, PlayerGameInfo


class GameForm(forms.ModelForm):
    riddle = forms.IntegerField(label='Загаданное число', required=False)

    class Meta:
        model = Game
        fields = ['riddle', ]

    def clean(self):
        # общая функция валидации
        return self.cleaned_data
