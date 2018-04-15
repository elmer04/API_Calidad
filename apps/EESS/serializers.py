from rest_framework.serializers import ModelSerializer
from apps.EESS.models import Eess

class EessSerializer(ModelSerializer):
    class Meta:
        model = Eess
        fields = '__all__'


