from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
from apps.usuario.models import Usuario, Diris


class UsuarioLogin(APIView):
    def post(self,request):
        usuario = request.data
        username=usuario['username']
        password=usuario['password']
        Estado={'idUsuario':'','Autorizado': False}
        try:
            user=Usuario.objects.get(user=username,password=password)
        except Usuario.DoesNotExist:
            return Response(Estado, status=status.HTTP_200_OK)
        Estado['Autorizado']=True
        Estado['idUsuario']=user.idusuario
        return Response(Estado, status=status.HTTP_201_CREATED)
