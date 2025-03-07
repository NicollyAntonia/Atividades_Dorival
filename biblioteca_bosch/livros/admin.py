from django.contrib import admin
from .models import Livro

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano_publicacao')  #vai ser exibido pro admin
    search_fields = ('titulo', 'autor')  #campo pesquis  pro admin

admin.site.register(Livro, LivroAdmin)
