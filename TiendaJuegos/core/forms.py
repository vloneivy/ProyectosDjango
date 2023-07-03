from django import forms
from django.forms import ModelForm, fields
from .models import Vehiculo

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['ID', 'marca', 'modelo', 'imagen', 'categoria']
