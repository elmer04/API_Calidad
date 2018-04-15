from django.db import models

# Create your models here.

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido_paterno = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45)
    user = models.CharField(max_length=45)
    password = models.TextField()
    correo = models.CharField(max_length=45)
    tipo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'

class Diris(models.Model):
    iddiris = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    usuario_idusuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, db_column='usuario_idusuario')

    class Meta:
        managed = False
        db_table = 'diris'


