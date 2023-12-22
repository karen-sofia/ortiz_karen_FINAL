from django import forms
from .models import Instituciones, Inscritos

class FormInstituciones(forms.ModelForm):
    class Meta:
        model = Instituciones
        fields = ['id', 'nombre']

class FormInscritos(forms.ModelForm):
    class Meta:
        model = Inscritos
        fields = ['id', 'nombre', 'telefono', 'fechaInscripcion', 'institucion', 'estado', 'observacion']

