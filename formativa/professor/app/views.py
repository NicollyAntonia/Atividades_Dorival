from rest_framework import viewsets, permissions
from .models import Professor, Disciplina, ReservaDeAmbiente
from .serializers import ProfessorSerializer, DisciplinaSerializer, ReservaSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requer login JWT
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = ReservaDeAmbiente.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
