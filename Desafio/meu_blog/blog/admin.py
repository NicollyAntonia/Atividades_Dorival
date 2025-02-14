from django.contrib import admin
from .models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'concluida', 'data_criacao')
    list_filter = ('concluida',)
    search_fields = ('descricao',)

admin.site.register(Tarefa, TarefaAdmin)

