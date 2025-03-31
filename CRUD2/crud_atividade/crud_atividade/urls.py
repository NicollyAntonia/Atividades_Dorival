from django.contrib import admin
from django.urls import path
from crud.views import lista_eventos, criar_eventos, atualizar_eventos, deletar_evento, detalhe_evento 

urlpatterns = [    
    path('admin/', admin.site.urls),
    path('eventos/', lista_eventos, name='lista_eventos'),
    path('eventos/criar/', criar_eventos, name='criar_eventos'),
    path('eventos/detalhe/<int:pk>/', detalhe_evento, name='detalhe_evento'),
    path('eventos/atualizar/<int:pk>/', atualizar_eventos, name='atualizar_eventos'),
    path('eventos/deletar/<int:pk>/', deletar_evento, name='deletar_evento'),
]
