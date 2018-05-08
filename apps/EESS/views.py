from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

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

class EESSRenaes(APIView):
    serializer=EessSerializer
    def get(self,request,renaes):
        try:
            eess = Eess.objects.get(renaes=renaes)
        except Eess.DoesNotExist:
            return Response('NO EXISTE RENAES',status=status.HTTP_400_BAD_REQUEST)
        response=self.serializer(eess)
        return Response(response.data)