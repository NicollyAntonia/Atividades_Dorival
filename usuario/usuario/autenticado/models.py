from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(models.Model):
    nome = models.CharField(max_length=10, blank = True, null = True)
    bio = models.TextField(max_length=200 , null=True, blank=True)
    endereco =  models.CharField(max_length=90, blank = True, null = True)
    idade = models.PositiveIntegerField()
    telefone = models.PositiveIntegerField()
    escolaridade = models.CharField(max_length=90, blank = True, null = True)
    quantidadeanimais = models.PositiveIntegerField()

    def __str__(self):
        return self.Usuario