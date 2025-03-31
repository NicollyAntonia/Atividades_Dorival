from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import evento
from .serializers import eventoSerializer

@api_view(['GET'])
def lista_eventos(request):
    # Filtros
    categoria = request.query_params.get('categoria', None)
    data = request.query_params.get('data', None)
    quantidade = request.query_params.get('quantidade', None)
    # Filtros de pesquisa
    eventos = evento.objects.all()
    # Filtragem por categoria
    if categoria:
        eventos = eventos.filter(categoria=categoria)
    # Filtragem por data
    if data:
        try:
            eventos = eventos.filter(data=data)
        except ValueError:
            return Response({"error": "Data inválida. Use o formato YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
    # Limitar a quantidade de resultados
    if quantidade:
        try:
            quantidade = int(quantidade)
            eventos = eventos[:quantidade]  # Limitar a quantidade de eventos retornados
        except ValueError:
            return Response({"error": "Quantidade deve ser um número inteiro."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Ordenação
    ordering = request.query_params.get('ordering', None)
    if ordering:
        eventos = eventos.order_by(ordering)

    serializer = eventoSerializer(eventos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def criar_eventos(request):
    if request.method == 'POST':
        serializer = eventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def atualizar_eventos(request, pk):
    try:
        evento_obj = evento.objects.get(pk=pk)  
    except evento.DoesNotExist:
        return Response({"error": "Evento não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    serializer = eventoSerializer(evento_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_evento(request, pk):
    try:
        evento_obj = evento.objects.get(pk=pk)
    except evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    evento_obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def detalhe_evento(request, pk):
    try:
        evento_obj = evento.objects.get(pk=pk)
    except evento.DoesNotExist:
        return Response({"error": "Evento não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = eventoSerializer(evento_obj)
    return Response(serializer.data)
