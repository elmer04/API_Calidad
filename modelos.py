# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Anotaciones(models.Model):
    idanotaciones = models.AutoField(primary_key=True)
    anotacion = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    anotacionescol = models.CharField(max_length=45, blank=True, null=True)
    eess_ideess = models.ForeignKey('Eess', models.DO_NOTHING, db_column='EESS_idEESS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anotaciones'


class Atributo(models.Model):
    idatributo = models.AutoField(primary_key=True)
    atributo = models.CharField(max_length=20, blank=True, null=True)
    idindicador = models.ForeignKey('Indicador', models.DO_NOTHING, db_column='idindicador')

    class Meta:
        managed = False
        db_table = 'atributo'


class Diris(models.Model):
    iddiris = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_idusuario')

    class Meta:
        managed = False
        db_table = 'diris'


class Eess(models.Model):
    ideess = models.AutoField(db_column='idEESS', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    gerente = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    renaes = models.CharField(max_length=45, blank=True, null=True)
    diris_iddiris = models.ForeignKey(Diris, models.DO_NOTHING, db_column='diris_iddiris')
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eess'


class Indicador(models.Model):
    idindicador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicador'


class MesesYear(models.Model):
    idfecha = models.AutoField(primary_key=True)
    mes = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'meses-year'



class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido_paterno = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45)
    user = models.CharField(max_length=45)
    password = models.TextField()
    correo = models.CharField(max_length=45)
    tipo = models.IntegerField()
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Valor(models.Model):
    idvalor = models.AutoField(primary_key=True)
    dato = models.FloatField(blank=True, null=True)
    idfecha = models.ForeignKey(MesesYear, models.DO_NOTHING, db_column='idfecha')
    ideess = models.ForeignKey(Eess, models.DO_NOTHING, db_column='idEESS')  # Field name made lowercase.
    idatributo = models.ForeignKey(Atributo, models.DO_NOTHING, db_column='idatributo')

    class Meta:
        managed = False
        db_table = 'valor'
        unique_together = (('idvalor', 'ideess', 'idatributo'),)
