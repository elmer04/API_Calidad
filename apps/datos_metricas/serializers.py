from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apps.datos_metricas.models import Valor, MesesYear, Atributo, Indicador, Resultados
from apps.EESS.serializers import EessSerializer

class IndicadorSerializer(ModelSerializer):
    class Meta:
        model = Indicador
        fields = '__all__'

class MesesYearSerializer(ModelSerializer):
    class Meta:
        model = MesesYear
        fields = '__all__'

class AtributoSerializer(ModelSerializer):
    class Meta:
        model = Atributo
        fields = '__all__'


class ValorSerializer(ModelSerializer):
    class Meta:
        model = Valor
        fields = '__all__'

class ResultadoSerializer(ModelSerializer):
    idindicador = serializers.SerializerMethodField()
    nombre = serializers.SerializerMethodField()

    def get_idindicador(self, resultado):
        atributo=Atributo.objects.get(idatributo=resultado.idatributo)
        return atributo.idindicador.idindicador
    def get_nombre(self,resultado):
        indicador = Atributo.objects.get(idatributo=resultado.idatributo).idindicador
        return indicador.nombre
    class Meta:
        model = Resultados
        fields = ('idindicador','nombre','color','porcentaje')

