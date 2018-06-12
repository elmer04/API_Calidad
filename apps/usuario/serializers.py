from rest_framework.serializers import ModelSerializer

from apps.usuario.models import Usuario, Diris


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class DirisSerializer(ModelSerializer):
    class Meta:
        model = Diris
        fields = '__all__'



