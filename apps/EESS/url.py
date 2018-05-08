from django.urls import path
from apps.EESS import views


app_name = 'eess'

urlpatterns = [
    path('renaes/<renaes>', views.EESSRenaes.as_view(), name='eess_renaes'),
    path('api', views.EESSList.as_view(), name='api_eesslist'),
]
