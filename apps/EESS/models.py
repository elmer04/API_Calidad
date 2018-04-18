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
    diris_iddiris = models.ForeignKey(Diris,on_delete=models.CASCADE, db_column='diris_iddiris')

    class Meta:
        managed = False
        db_table = 'EESS'

class Anotaciones(models.Model):
    idanotaciones = models.AutoField(primary_key=True)
    anotacion = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    anotacionescol = models.CharField(max_length=45, blank=True, null=True)
    eess_ideess = models.ForeignKey(Eess,on_delete=models.CASCADE, db_column='EESS_idEESS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anotaciones'




class VisitasEess(models.Model):
    idvisitas = models.AutoField(primary_key=True)
    observacion = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    eess_ideess = models.ForeignKey(Eess,on_delete=models.CASCADE, db_column='EESS_idEESS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visitas-eess'
        #unique_together = (('idvisitas', 'eess_ideess'),)

class Horario(models.Model):
    idhorario = models.AutoField(primary_key=True)
    prioridad = models.IntegerField()
    eess_ideess = models.ForeignKey(Eess,on_delete=models.CASCADE, db_column='EESS_idEESS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'horario'