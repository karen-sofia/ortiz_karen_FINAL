from rest_framework import serializers
from seminario_app import models

class InstitucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instituciones
        fields = '__all__'

class InscritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inscritos
        fields = '__all__'

