from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, widget=forms.TextInput(
        attrs={
            'id': 'registerEmail',
            'class': 'form-control form-control-lg',
            'placeholder': '*E-Mail',
        }
    ))
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput(
        attrs={
            'id': 'registerPassword1',
            'class': 'form-control form-control-lg',
            'placeholder': '*Passwort',
        }
    ))
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput(
        attrs={
            'id': 'registerPassword2',
            'class': 'form-control form-control-lg',
            'placeholder': '*Passwort wiederholen',
        }
    ))

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
