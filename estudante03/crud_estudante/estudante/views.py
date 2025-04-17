from django.shortcuts import render
from .models import Aluno
from .serializers import AlunosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#fizemos hoje
@api_view(['GET'])
def detalhe_aluno(request,pk):
    try:
        aluno = Aluno.objects.get(pk=pk)
    except Aluno.DoesNotExist:
            return Response('erro: nao encontrei esse aluno do dorival',status=status.HTTP_404_NOT_FOUND)
    
    serializer=AlunosSerializer(aluno)
    return Response (serializer.data, status=status.HTTP_200_OK)
#até aqui


@api_view(['GET'])
def listar_alunos(request):
    alunos= Aluno.objects.all()
    serializer= AlunosSerializer(alunos, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def criar_alunos(request):
    if request.method=='POST':
        serializer=AlunosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


#fizemos hoje
@api_view(['PUT'])
def alterar_aluno(request,pk):
    try:
          aluno = Aluno.objects.get(pk=pk)
    except Aluno.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=AlunosSerializer(aluno,data=request.data)
    if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_informacoes(request,pk):
    try:
          aluno=Aluno.objects.get(pk=pk)
    except Aluno.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
    aluno.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def macharete(request,texto):
     import pyfiglet 
     gabriel=pyfiglet.figlet_format(texto)
     tipo = request.query_params.get('type')
     return Response({'tipo': tipo, 'gabriel': gabriel},status=status.HTTP_200_OK)
