from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    class Meta:
        model = Banks
        fields = ['username', 'first_name', 'branch', 'IFSC', 'email', 'password1', 'password2']