from django import forms
from .models import Instituciones, Inscritos

class FormInstituciones(forms.ModelForm):
    class Meta:
        model = Instituciones
        fields = '__all__'
        
class FormInscritos(forms.ModelForm):
    class Meta:
        model = Inscritos
        fields = ['id', 'nombre', 'telefono', 'institucion', 'estado', 'observacion']
        
