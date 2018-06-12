from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
from apps.usuario.models import Usuario, Diris, TipoUsuario
from apps.usuario.serializers import UsuarioSerializer, DirisSerializer


class UsuarioLogin(APIView):
    def post(self,request):
        usuario = request.data
        username=usuario['username']
        password=usuario['password']
        Estado={'idUsuario':'','Autorizado': False,'tipo_usuario':''}
        try:
            user=Usuario.objects.get(user=username,password=password)
        except Usuario.DoesNotExist:
            return Response(Estado, status=status.HTTP_200_OK)
        Estado['Autorizado']=True
        Estado['idUsuario']=user.idusuario
        Estado['tipo_usuario']=user.tipo.nombre
        return Response(Estado, status=status.HTTP_201_CREATED)

class getUser(APIView):
    serializer_user=UsuarioSerializer
    serializer_diris = DirisSerializer
    def get(self,request,id):
        user=Usuario.objects.get(idusuario=id)
        response={}
        response['usuario']=(self.serializer_user(user)).data
        #if user.tipo.nombre=='administrador' :
        if user.tipo.nombre == 'usuario':
            diris=Diris.objects.get(usuario_idusuario=user.idusuario)
            response['diris'] = (self.serializer_diris(diris)).data
        return Response(response,status=status.HTTP_200_OK)

