import traceback
from os import rename

from django.shortcuts import render
from django.db import  connection
from rest_framework.views import APIView
from django.http import  HttpResponse
from Algoritmos.algoritmos_bd import dictfetchall
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
            print(request.data)
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
                        print(eess['nombre'])
                        renaes = Eess.objects.get(nombre=eess['nombre'])
                    except Eess.DoesNotExist:
                        renaes=''
                        if 'renaes' in eess.keys():
                            print("crear sin renaes")
                            renaes=eess['renaes']
                        renaes = Eess.objects.create(
                            nombre=eess['nombre'],
                            tipo=1,
                            gerente='Steve',
                            direccion='Mi casa',
                            renaes=renaes,
                            diris_iddiris=Diris.objects.get(iddiris=1)
                        )
                        print("CREADO "+eess['nombre'])
                    for atributo in atributos:
                        idatributo = Atributo.objects.get(idatributo=atributo['idatributo'])
                        valor = eess[atributo['atributo']]
                        #Valor.objects.create(
                         #   dato=valor,
                          #  idfecha=datoMesYear.idfecha,
                          #  ideess=renaes.ideess,
                          #  idatributo=idatributo.idatributo
                        #)
                        if(not valor):
                            valor=0;
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

class MetricasUpdate(APIView):
    def post(self,request):
        metricas = request.data
        for metrica in metricas:
            Indicador.objects.filter(idindicador=metrica['idindicador']).update(nombre=metrica['nombre'])
        return Response("Metricas subida con exito", status=status.HTTP_201_CREATED)

class ponerColor(APIView):
    def get(self,request,metrica):
        atributo=Atributo.objects.get(idindicador=metrica,atributo='pct')
        cur = connection.cursor()
        fechas=MesesYear.objects.all()
        for fecha in fechas :
            cur.callproc('max_min', [fecha.idfecha,atributo.idatributo])
        cur.close()
        return Response("Procedure completado")

class ListFechas(APIView):
    def get(self,request):
        sql="select idfecha,CONCAT(LPAD(mes,2,'0'),'-',year) as fecha from `meses-year` order by idfecha desc"
        cursor = connection.cursor()
        cursor.execute(sql)
        datos=dictfetchall(cursor)
        cursor.close()
        return Response(datos,status=status.HTTP_200_OK)

