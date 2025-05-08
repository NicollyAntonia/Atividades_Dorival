from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.conf import settings

class Professor(AbstractUser):
    ni = models.PositiveIntegerField(unique=True)
    nome = models.CharField(max_length=300)
    email = models.EmailField(blank=True,null=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField()

    groups = models.ManyToManyField(
        Group,
        related_name='professor_groups',  
        blank=True,
        help_text='As groups this user belongs to.',
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
        return self.nome
    
class Disciplinar (models.Model):
    curso_escolhas = [
        ('ADS', 'Análise e Desenvolvimento de Sistemas'),
        ('ENG', 'Engenharia'),
        ('ADM', 'Administração'),
    ]
    curso = models.CharField(max_length=50, choices=curso_escolhas)
    nome = models.CharField(max_length=300,)
    carga_horaria = models.TimeField()
    descricao = models.CharField(max_length=500, blank=True, null=True)
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,related_name='Disciplinas',null=True)
   
    def __str__(self):
        return self.nome

class ReservaDeAmbiente(models.Model):
    periodo_escolhas = [
        ('M','Manhã'),
        ('T','Tarde'),
        ('N','Noite'),
    ]
    periodo = models.CharField(max_length=1, choices=periodo_escolhas)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    sala_reservada = models.IntegerField()
    professor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,related_name='Reservas',null=True)
    disciplina = models.ForeignKey(Disciplinar,on_delete=models.SET_NULL,related_name='Reservas',null=True)

    def __str__(self):
        return f"{self.sala_reservada} - {self.get_periodo_display()} ({self.data_inicio})"
    