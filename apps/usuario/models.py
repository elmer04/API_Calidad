from django.db import models

# Create your models here.

class TipoUsuario(models.Model):
    idtipo_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido_paterno = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45)
    user = models.CharField(max_length=45)
    password = models.TextField()
    correo = models.CharField(max_length=45)
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.DO_NOTHING, db_column='tipo')

    class Meta:
        managed = False
        db_table = 'usuario'

class Diris(models.Model):
    iddiris = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    usuario_idusuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING, db_column='usuario_idusuario')

    class Meta:
        managed = False
        db_table = 'diris'


