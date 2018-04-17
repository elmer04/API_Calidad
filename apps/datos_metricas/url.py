from django.urls import path
from apps.datos_metricas import views


app_name='datosmetricas'

urlpatterns = [
    path('api/<pk>', views.Datos_Metricas.as_view(),name='api_datosmetricas'),
]
