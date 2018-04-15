from django.shortcuts import render
from rest_framework.views import APIView
from django.http import  HttpResponse
from apps.datos_metricas.serializers import ValorSerializer
from rest_framework.response import Response
from apps.datos_metricas.models import MesesYear,Atributo,Indicador,Valor
from apps.EESS.models import Eess
from rest_framework import status

# Create your views here.
class Datos_Metricas(APIView):
    serializer=ValorSerializer
    def get(self,request):
        valores=Valor.objects.all()
        response=self.serializer(valores,many=True)
        return Response(response.data)
    def post(self, request):
        json=request.data
        datosmetrica=json['valoresmetricas']
        try :
            idmetrica=Indicador.objects.get(nombre=json['metrica']).idindicador
        except Indicador.DoesNotExist:
            Response('INDICADOR NO EXISTE', status=status.HTTP_400_BAD_REQUEST)


        atributos=Atributo.objects.filter(idindicador=idmetrica).values('atributo','idatributo')
        for datometrica in datosmetrica:
            mes=datometrica['mes']
            year=datometrica['anio']
            try:
                datoMesYear = MesesYear.objects.get(mes=mes, year=year)
            except MesesYear.DoesNotExist:
                datoMesYear=MesesYear.objects.create(
                                        mes=mes,
                                        year=year
                                        )
            eess=datometrica['eess']
            try:
                datoEess = Eess.objects.get(nombre=eess)
            except Eess.DoesNotExist:
                return Response('EESS NO EXISTE', status=status.HTTP_400_BAD_REQUEST)
            datos=datometrica['datos']
            for key, value in datos.items():
                for atributo in atributos:
                    if key == atributo['atributo']:
                        idatributo = Atributo.objects.get(idatributo=atributo['idatributo'])
                        Valor.objects.create(
                                            dato=value,
                                            idfecha=datoMesYear,
                                            ideess=datoEess,
                                            idatributo=idatributo
                                            )
                        break
                else:
                    return Response('Atributo no encontrado',status.HTTP_400_BAD_REQUEST)
        return Response('DATOS GUARDADO CORRECTAMENTE',status=status.HTTP_201_CREATED)

    #def post(self, request, pk):