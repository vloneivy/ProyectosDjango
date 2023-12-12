from django import forms
from django.forms import ModelForm, fields
from .models import servicio

class servicioForm(ModelForm):
    class Meta:
        model = servicio
        fields = ['codigo', 'nombre', 'servicios', 'imagen', 'categoria']
