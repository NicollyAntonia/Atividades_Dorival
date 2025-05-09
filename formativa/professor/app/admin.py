from django.contrib import admin
from .models import Professor, Disciplina, ReservaDeAmbiente
from django.contrib.auth.admin import UserAdmin

@admin.register(Professor)
class ProfessorAdmin(UserAdmin):
    model = Professor
    list_display = ('username', 'name', 'ni', 'email', 'telefone')
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {
            'fields': ('ni', 'name', 'telefone', 'data_nascimento', 'data_contratacao')
        }),
    )

admin.site.register(Disciplina)
admin.site.register(ReservaDeAmbiente)
