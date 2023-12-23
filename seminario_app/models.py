from django.db import models

# Create your models here.

class Instituciones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre)

class Inscritos(models.Model):
    

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fechaInscripcion = models.DateField( auto_now_add=True)
    institucion = models.ForeignKey(Instituciones, on_delete=models.PROTECT)
    horaInscripcion = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO ASISTEN', 'No Asisten')])
    observacion = models.CharField(max_length=500)

