from django.db import models
from apps.usuario.models import Diris

# Create your models here.

class Eess(models.Model):
    ideess = models.AutoField(db_column='idEESS', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    gerente = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    renaes = models.CharField(max_length=45, blank=True, null=True)
    diris_iddiris = models.ForeignKey(Diris,on_delete=models.DO_NOTHING, db_column='diris_iddiris')
    estado = models.IntegerField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EESS'

class Anotaciones(models.Model):
    idanotaciones = models.AutoField(primary_key=True)
    anotacion = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    titulo = models.CharField(max_length=45, blank=True, null=True)
    #contenido  JSON ( SE MANEJA DIRECTAMENT EN QUERY POR MOTIVOS DE RAPIDEZ)
    eess_ideess = models.ForeignKey(Eess,on_delete=models.DO_NOTHING, db_column='EESS_idEESS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anotaciones'


