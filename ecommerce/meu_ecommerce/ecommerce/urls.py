from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('produto/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
]
