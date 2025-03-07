from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm

#oiiiiiiiiiii dorivas 
#essas classes vao fazer as coisas funcionar e definir se sao get ou um post(isso so pq o dorival pediu) 

def listar_livros(request):
    livros = Livro.objects.all() 
    return render(request, 'livros/listar_livros.html', {'livros': livros})


def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/cadastrar_livro.html', {'form': form})

def atualizar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/atualizar_livro.html', {'form': form})

def remover_livro(request, pk):  
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        livro.delete() 
        return redirect('listar_livros')  
    return render(request, 'livros/remover_livro.html', {'livro': livro}) 



