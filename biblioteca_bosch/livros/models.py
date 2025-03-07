from django.db import models

#essa classe esta definindo os tamanhos maximos pra cada campo pq se nao o usuario vai escrever mais que eu
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
