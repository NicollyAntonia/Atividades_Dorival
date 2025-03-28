from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import UserAbs
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password or not email:
        return Response({'Erro': 'Informações insuficientes'}, status=status.HTTP_400_BAD_REQUEST)

    if UserAbs.objects.filter(username=username).exists():
        return Response({"Erro": 'Username já existe'}, status=status.HTTP_400_BAD_REQUEST)

    if UserAbs.objects.filter(email=email).exists():
        return Response({"Erro": 'Email já utilizado'}, status=status.HTTP_400_BAD_REQUEST)

    usuario = UserAbs.objects.create_user(
        username=username,
        email=email,
        password=password,
    )
    return Response({"Mensagem": f"Usuário {username} criado com sucesso"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logar(request):
    username = request.data.get('username')
    password = request.data.get('password')
    usuario = authenticate(username=username, password=password)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Usuário ou senha inválidos'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_protegida(request):
    return Response({"Mensagem": "Ola"}, status=status.HTTP_200_OK)
