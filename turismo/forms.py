from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import LugarTuristico

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LugarForm(forms.ModelForm):
    class Meta:
        model = LugarTuristico
        fields = ['nombre', 'ciudad', 'categoria', 'descripcion', 'imagen']