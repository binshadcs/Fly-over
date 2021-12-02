from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class BankRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    class Meta:
        model = customers
        fields = ['username', 'first_name', 'email', 'password1', 'password2']