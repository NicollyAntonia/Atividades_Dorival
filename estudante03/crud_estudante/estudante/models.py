from django.db import models

class Aluno(models.Model):
    nome=models.CharField(max_length=150)
    idade=models.PositiveBigIntegerField()
    curso=models.CharField(max_length=50)
    instituicao=models.CharField(max_length=100)
    rm=models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.rm}--{self.nome}'
