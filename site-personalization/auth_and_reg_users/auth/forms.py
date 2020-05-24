from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

from .models import CustomUser


class SignupForm(UserCreationForm):

    class Meta(object):
        model = CustomUser
        fields = ('username', 'password1', 'password2')


