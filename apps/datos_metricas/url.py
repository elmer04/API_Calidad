from django.urls import path
from apps.datos_metricas import views


app_name='datosmetricas'

urlpatterns = [
    path('api/<pk>', views.Datos_Metricas.as_view(),name='api_datosmetricas'),
    path('metricas', views.MetricasListCreate.as_view(), name='getlist_create_metricas'),
    path('metrica/<pk>', views.MetricaUpdate.as_view(), name='get_update_metricas'),
]
