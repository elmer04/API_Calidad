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
    def get(self,request,pk):
        valores=Valor.objects.all()
        response=self.serializer(valores,many=True)
        return Response(response.data)
    def post(self, request,pk):
        json=request.data
        datosmetrica=json['months']
        anio = json['year']

        atributos=Atributo.objects.filter(idindicador=pk).values('atributo','idatributo')
        for valor_metrica in datosmetrica:
            mes=valor_metrica['month']
            try:
                datoMesYear = MesesYear.objects.get(mes=mes, year=anio)
            except MesesYear.DoesNotExist:
                datoMesYear=MesesYear.objects.create(
                                        mes=mes,
                                        year=anio
                                        )
            valores_eess=valor_metrica['eess']

            for eess in valores_eess:

                try:
                    renaes=Eess.objects.get(nombre=eess['nombre'])
                except Eess.DoesNotExist:
                    return Response('EESS NO EXISTE', status=status.HTTP_400_BAD_REQUEST)

                for atributo in atributos:
                    idatributo = Atributo.objects.get(idatributo=atributo['idatributo'])
                    valor=eess[atributo['atributo']]
                    Valor.objects.create(
                        dato=valor,
                        idfecha=datoMesYear,
                        ideess=renaes,
                        idatributo=idatributo
                    )


    #def post(self, request, pk):