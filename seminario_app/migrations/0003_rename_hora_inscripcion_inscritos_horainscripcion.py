# Generated by Django 4.2.6 on 2023-12-22 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminario_app', '0002_alter_inscritos_institucion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscritos',
            old_name='hora_inscripcion',
            new_name='horaInscripcion',
        ),
    ]
