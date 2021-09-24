from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from django import forms


class register_form(forms.Form):
    email = forms.CharField(max_length = 200)
    password = forms.CharField(max_length = 200)