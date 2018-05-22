import traceback
from os import rename

from django.shortcuts import render
from django.db import  connection
from rest_framework.views import APIView
from django.http import  HttpResponse
from apps.datos_metricas.serializers import ValorSerializer, IndicadorSerializer
from rest_framework.response import Response
from apps.datos_metricas.models import MesesYear,Atributo,Indicador,Valor
from apps.usuario.models import Diris
from apps.EESS.models import Eess
from rest_framework import status,generics

# Create your views here.
class Datos_Metricas(APIView):
    serializer=ValorSerializer
    def get(self,request,pk):
        valores=Valor.objects.all()
        response=self.serializer(valores,many=True)
        #return Response(response.data)
        return Response()

    def post(self, request,pk):
        """
        #ALGORITMO TERMINADO ( adios vaquero :'v)
        try:
            json=request.data[0]
            datosmetrica = json['months']
            anio = json['year']
            atributos = Atributo.objects.filter(idindicador=pk).values('atributo', 'idatributo')

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
                        renaes=Eess.objects.get(renaes=eess['renaes'])
                    except Eess.DoesNotExist:
                        renaes=Eess.objects.create(
                                                nombre = eess['nombre'],
                                                tipo = 1,
                                                gerente = 'Steve',
                                                direccion = 'Mi casa',
                                                renaes = eess['renaes'],
                                                diris_iddiris = Diris.objects.get(iddiris=1)
                                            )
                    for atributo in atributos:
                        idatributo = Atributo.objects.get(idatributo=atributo['idatributo'])
                        valor=eess[atributo['atributo']]
                        Valor.objects.create(
                            dato=valor,
                            idfecha=datoMesYear.idfecha,
                            ideess=renaes.ideess,
                            idatributo=idatributo.idatributo
                        )
                        print('valor ingresado con exito')

            return Response(request.data,status=status.HTTP_201_CREATED)
        except KeyError as e:
            print(traceback.format_exc())
            return Response("Formato equivocado" ,status= status.HTTP_400_BAD_REQUEST)
        """
        try:
            #algoritmo MEJORADO DE 10 SEGUNDOS por excel
            cursor=connection.cursor()
            json = request.data[0]
            datosmetrica = json['months']
            anio = json['year']
            atributos = Atributo.objects.filter(idindicador=pk).values('atributo', 'idatributo')
            contador=0
            values=[]
            for valor_metrica in datosmetrica:
                mes = valor_metrica['month']
                try:
                    datoMesYear = MesesYear.objects.get(mes=mes, year=anio)
                except MesesYear.DoesNotExist:
                    datoMesYear = MesesYear.objects.create(
                        mes=mes,
                        year=anio
                    )
                valores_eess = valor_metrica['eess']
                for eess in valores_eess:
                    try:
                        renaes = Eess.objects.get(renaes=eess['renaes'])
                    except Eess.DoesNotExist:
                        renaes = Eess.objects.create(
                            nombre=eess['nombre'],
                            tipo=1,
                            gerente='Steve',
                            direccion='Mi casa',
                            renaes=eess['renaes'],
                            diris_iddiris=Diris.objects.get(iddiris=1)
                        )
                    for atributo in atributos:
                        idatributo = Atributo.objects.get(idatributo=atributo['idatributo'])
                        valor = eess[atributo['atributo']]
                        #Valor.objects.create(
                         #   dato=valor,
                          #  idfecha=datoMesYear.idfecha,
                          #  ideess=renaes.ideess,
                          #  idatributo=idatributo.idatributo
                        #)
                        value=[valor,
                               datoMesYear.idfecha,
                               renaes.ideess,
                               idatributo.idatributo]
                        values.append(value)
                        contador = contador + 1
                        print(contador)
            cursor.executemany('INSERT INTO valor (dato, idfecha, idEESS,idatributo) VALUES (%s, %s, %s,%s)', values)
            cursor.close()
            print('transaccion COMPLETADA ! ')
            return Response("transaccion completada",status=status.HTTP_201_CREATED)
        except KeyError:
            print(traceback.format_exc())
            return Response("Formato equivocado", status=status.HTTP_400_BAD_REQUEST)

class MetricasListCreate(generics.ListCreateAPIView):
    serializer_class = IndicadorSerializer
    queryset = Indicador.objects.all()

class MetricaUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = IndicadorSerializer
    queryset = Indicador.objects.all()