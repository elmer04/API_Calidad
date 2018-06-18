from django.urls import path
from apps.EESS import views


app_name = 'eess'

urlpatterns = [
    path('api/<int:iddiris>', views.EESSList.as_view(), name='api_eesslist'),
    path('renaes/<int:iddiris>/<str:renaes>', views.EESSgetRenaes.as_view(), name='api_eess_renaes'),
    path('nombre/<int:iddiris>/<str:nombre>', views.EESSgetNombre.as_view(), name='api_eess_nombre'),
    path('eessMetricaColor/<int:iddiris>/<int:metrica>/<str:color>', views.EESSMetricaColor.as_view(), name='api_eess_metrica_color'),
    path('eessMetricaColor/<int:iddiris>/<int:metrica>', views.EESSMetricaColor.as_view(), name='api_eess_metrica_color'),
    path('eessMetricaColorFecha/<int:ideess>/<int:idfecha>', views.EESSMetricasColorFecha.as_view(), name='api_eess_metrica_color_fecha'),
    path('notas/<int:ideess>/<int:idfecha>', views.EessNotas.as_view(), name='api_eess_notas'),
]
