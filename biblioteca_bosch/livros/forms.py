from django import forms
from .models import Livro

#coloca os campos a serem preenchidos como os da ultima linha
#fiz pq sem isso o usuario nao consegue fazer nada e so o admin iria conseguir cadastrar livros e pro dorivas poder ver essa coisa maravilhosa com o melhor design do mundo
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano_publicacao', 'descricao']
