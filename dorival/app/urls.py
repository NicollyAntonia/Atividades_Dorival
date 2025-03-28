from django.urls import path
from . import views

urlpatterns = [
    path('criarUsuario/', views.create_user, name='create_user'),
    path('logar/', views.logar, name='logar'),
    path('view_protegida/', views.view_protegida, name='view_protegida'),
]
