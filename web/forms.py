from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Person

class Send(ModelForm):
    class Meta:
        model = Person
        fields = ('first_name' , 'last_name' , 'email' , 'number' , 'zip')