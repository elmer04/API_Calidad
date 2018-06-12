from django.urls import path
from apps.usuario import views

app_name = 'usuario'

urlpatterns = [
    path('login', views.UsuarioLogin.as_view(), name='api_eesslist'),
    path('getUser/<int:id>', views.getUser.as_view(), name='api_getUser'),
]
