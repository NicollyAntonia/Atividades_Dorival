from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

class Professor(AbstractUser):
    ni = models.PositiveIntegerField(unique=True, default=99999)
    name = models.CharField(max_length=300,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=15,blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    data_contratacao = models.DateField(blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='professor_groups',
        blank=True,
        help_text='Groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='professor_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.name


class Disciplina(models.Model):
    curso_escolhas = [
        ('ADS', 'Análise e Desenvolvimento de Sistemas'),
        ('ENG', 'Engenharia'),
        ('ADM', 'Administração'),
    ]
    curso = models.CharField(max_length=50, choices=curso_escolhas)
    name = models.CharField(max_length=300)
    carga_horaria = models.IntegerField()  # em horas
    descricao = models.CharField(max_length=500, blank=True, null=True)
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='disciplinas', null=True)

    def __str__(self):
        return self.name


class ReservaDeAmbiente(models.Model):
    periodo_escolhas = [
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    ]
    periodo = models.CharField(max_length=1, choices=periodo_escolhas)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    sala_reservada = models.IntegerField()
    professor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='reservas', null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, related_name='reservas', null=True)

    def __str__(self):
        return f"Sala {self.sala_reservada} - {self.get_periodo_display()} ({self.data_inicio})"
