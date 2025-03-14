from django.db import models


class evento(models.Model):
    class Categoria(models.TextChoices):
        MUSICA = 'Música', 'Música'
        TEATRO = 'Teatro', 'Teatro'
        CINEMA = 'Cinema', 'Cinema'
        ARTE = 'Arte', 'Arte'

    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=500)
    data = models.DateTimeField()
    local = models.CharField(max_length=250)
    categoria = models.CharField(max_length=7, choices=Categoria.choices)

    def __str__(self):
        return f'{self.nome}--{self.categoria}'