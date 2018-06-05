from django.shortcuts import render
from rest_framework import status,generics
from rest_framework.response import Response
from apps.datos_metricas.models import MesesYear, Resultados, Indicador, Atributo
from rest_framework.views import APIView
from apps.EESS.models import Eess
from apps.EESS.serializers import EessSerializer

# Create your views here.


class EESSList(APIView):
    serializer=EessSerializer
    def get(self,request):
        eess=Eess.objects.all()
        response=self.serializer(eess,many=True)
        return Response(response.data)


class EESSMetricaColor(APIView):
    serializer=EessSerializer
    def get(self,request,metrica,color=''):
        #metrica=1
        atributo=Atributo.objects.get(idindicador=metrica, atributo="pct")
        MesYear=MesesYear.objects.all().reverse()[0]
        if color != '' :
            resultado=Resultados.objects.filter(color=color,idfecha=MesYear.idfecha,idatributo=atributo.idatributo)
        else:
            resultado =Resultados.objects.filter(idfecha=MesYear.idfecha,idatributo=atributo.idatributo)
        response=[]
        for resul in resultado:
            eess=Eess.objects.get(ideess=resul.ideess)
            json=(self.serializer(eess)).data
            json['color']=resul.color
            json['porcentaje']=resul.porcentaje
            response.append(json)
        return Response(response)

class EESSgetRenaes(generics.RetrieveAPIView):
    lookup_field = 'renaes'
    queryset = Eess.objects.all()
    serializer_class = EessSerializer

class EESSgetNombre(generics.RetrieveAPIView):
    lookup_field = 'nombre'
    queryset = Eess.objects.all()
    serializer_class = EessSerializer



