from rest_framework import serializers
from .models import evento

class eventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = evento
        fields = ['id', 'nome', 'descricao', 'data', 'local', 'categoria']
