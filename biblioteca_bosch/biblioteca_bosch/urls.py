from django.contrib import admin
from django.urls import path, include
from livros import views

#urls para cadastrar editar e remover , e tudo isso so pq o dorival quis
urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/', include('livros.urls')),
    path('', views.listar_livros, name='listar_livros'),
    path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
    path('editar/<int:pk>/', views.atualizar_livro, name='editar_livro'),
    path('remover/<int:pk>/', views.remover_livro, name='remover_livro'),

]
