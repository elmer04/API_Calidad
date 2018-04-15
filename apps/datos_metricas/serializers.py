from rest_framework.serializers import ModelSerializer
from apps.datos_metricas.models import Valor,MesesYear,Atributo,Indicador
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

