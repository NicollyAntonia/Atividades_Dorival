from rest_framework import serializers
from .models import Professor, Disciplina, ReservaDeAmbiente

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'ni', 'username', 'name', 'email', 'telefone', 'data_nascimento', 'data_contratacao']

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['id', 'curso', 'name', 'carga_horaria', 'descricao', 'responsavel']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaDeAmbiente
        fields = ['id', 'periodo', 'data_inicio', 'data_fim', 'sala_reservada', 'professor', 'disciplina']
