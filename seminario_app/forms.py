from django import forms
from .models import Instituciones, Inscritos

class FormInstituciones(forms.ModelForm):
    class Meta:
        model = Instituciones
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FormInscritos(forms.ModelForm):
    class Meta:
        model = Inscritos
        fields = ['id', 'nombre', 'telefono', 'institucion', 'estado', 'observacion']
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'institucion': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observacion': forms.TextInput(attrs={'class': 'form-control'}),
        }
