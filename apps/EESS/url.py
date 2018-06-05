from django.urls import path
from apps.EESS import views


app_name = 'eess'

urlpatterns = [
    path('api', views.EESSList.as_view(), name='api_eesslist'),
    path('renaes/<renaes>', views.EESSgetRenaes.as_view(), name='api_eess_renaes'),
    path('nombre/<nombre>', views.EESSgetNombre.as_view(), name='api_eess_nombre'),
    path('eessMetricaColor/<int:metrica>/<str:color>', views.EESSMetricaColor.as_view(), name='api_eess_metrica_color'),
    path('eessMetricaColor/<int:metrica>', views.EESSMetricaColor.as_view(), name='api_eess_metrica_color'),
]
