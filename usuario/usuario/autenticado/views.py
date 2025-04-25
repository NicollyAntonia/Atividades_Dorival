from django.shortcuts import render
from .models import Usuario
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers,status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UsuarioSerializers, LoginSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView

class UsuarioPaginacao(PageNumberPagination):
    page_size=2
    page_size_query_param = 'page_size'
    max_page_size =  3

class LoginView(TokenObtainPairView):
    serializer_class=LoginSerializer

class UsuarioListCreatAPIView(ListCreateAPIView):
    queryset= Usuario.objects.all()
    serializer_class=UsuarioSerializers
    pagination_class= UsuarioPaginacao
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset =  super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome :                                             
            queryset = queryset.filter(nome__icontains = nome)# 
        return queryset  
    
    def perform_create(self, serializer):
        if serializer.validated_data['idade']<0:
            raise serializers.ValidationError("A idade não pode ser negativa")
        if serializer.validated_data['quantidade de pets']<0:
            raise serializers.ValidationError("A quantidade de pets não pode ser negativa")
        
        serializer.save()


class UsuarioRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset= Usuario.objects.all()
    serializer_class = UsuarioSerializers
    lookup_field = 'pk'
    def put(self, request, *args, **kwargs):
        idade = request.data.get('idade')
        if idade>=20:
            data = request.data.copy
            data['escolaridade']=['Ensino Médio Completo']
            request.__full_data=data
        return super().put(request, *args, **kwargs)