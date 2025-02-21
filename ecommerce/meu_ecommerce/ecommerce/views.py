from django.shortcuts import render, get_object_or_404
from .models import Produto

#lista todos os produtos
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'ecommerce/lista_produtos.html', {'produtos': produtos})

#exibe os detalhes de um produto
def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'ecommerce/detalhe_produto.html', {'produto': produto})
