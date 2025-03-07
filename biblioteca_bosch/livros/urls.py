from django.urls import path
from . import views

#urls que redirecionam para a função respectiva exibindo ela, e dessa vex fiz pq e preciso e nao pq o dorival pediu
urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
    path('atualizar/<int:pk>/', views.atualizar_livro, name='atualizar_livro'),
    path('remover/<int:pk>/', views.remover_livro, name='remover_livro'), 
]
