from django.shortcuts import render
from rest_framework import status,generics
from rest_framework.response import Response
from apps.datos_metricas.models import MesesYear, Resultados, Indicador, Atributo
from rest_framework.views import APIView
from apps.EESS.models import Eess
from apps.EESS.serializers import EessSerializer

# Create your views here.
from apps.datos_metricas.serializers import ResultadoSerializer


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
        MesYear=MesesYear.objects.all().order_by('-idfecha')[0]
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

class EESSgetRenaes(APIView):
    serializerEess= EessSerializer
    serializerResultado =ResultadoSerializer
    def get(self,request,renaes):
        try:
            eess=Eess.objects.get(renaes=renaes)
        except Eess.DoesNotExist:
            return Response('NO EXISTE EL CENTRO DE SALUD',status=status.HTTP_400_BAD_REQUEST)
        MesYear = MesesYear.objects.all().order_by('-idfecha')[0]
        resultados=Resultados.objects.filter(ideess=eess.ideess,idfecha=MesYear.idfecha)
        resultadoResponse = (self.serializerResultado(resultados,many=True)).data
        response=(self.serializerEess(eess)).data
        response['metricas']=resultadoResponse
        return Response(response,status=status.HTTP_200_OK)

class EESSgetNombre(APIView):
    serializerEess= EessSerializer
    serializerResultado =ResultadoSerializer
    def get(self,request,nombre):
        try:
            eess=Eess.objects.get(nombre=nombre)
        except Eess.DoesNotExist:
            return Response('NO EXISTE EL CENTRO DE SALUD',status=status.HTTP_400_BAD_REQUEST)
        MesYear = MesesYear.objects.all().order_by('-idfecha')[0]
        resultados=Resultados.objects.filter(ideess=eess.ideess,idfecha=MesYear.idfecha)
        resultadoResponse = (self.serializerResultado(resultados,many=True)).data
        response=(self.serializerEess(eess)).data
        response['metricas']=resultadoResponse
        return Response(response,status=status.HTTP_200_OK)



