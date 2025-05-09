from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProfessorViewSet, DisciplinaViewSet, ReservaViewSet

professor_list = ProfessorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
professor_detail = ProfessorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

disciplina_list = DisciplinaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
disciplina_detail = DisciplinaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

reserva_list = ReservaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
reserva_detail = ReservaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('professores/', professor_list, name='professor-list'),
    path('professores/<int:pk>/', professor_detail, name='professor-detail'),

    path('disciplinas/', disciplina_list, name='disciplina-list'),
    path('disciplinas/<int:pk>/', disciplina_detail, name='disciplina-detail'),

    path('reservas/', reserva_list, name='reserva-list'),
    path('reservas/<int:pk>/', reserva_detail, name='reserva-detail'),
])
