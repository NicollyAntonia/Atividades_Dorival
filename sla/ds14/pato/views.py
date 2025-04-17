from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import Pato
from .serializers import PatoSerializers, LoginSerializer, DonoDoPatoSerializer, LoginSerializer2
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers,status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

class PatoPaginacao(PageNumberPagination):
    page_size=3
    page_size_query_param = 'page_size'
    max_page_size = 3



class PatoListCreatAPIView(ListCreateAPIView):
    queryset= Pato.objects.all()
    serializer_class=PatoSerializers
    pagination_class= PatoPaginacao
    permission_classes = [IsAuthenticated]

    def get_queryset(self):# |_______________
        queryset =  super().get_queryset()# |__________ NÃO PRECISA DESSA PARTE
        nome = self.request.query_params.get('nome')# |___________
        if nome : #                                              |
            queryset = queryset.filter(nome__icontains = nome)# |______
        return queryset                                   #           |
    
    def perform_create(self, serializer):
        if serializer.validated_data['peso']<0:
            raise serializers.ValidationError("O peso não pode ser negativo")
        serializer.save()

class PatoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset =  Pato.objects.all()
    serializer_class = PatoSerializers
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        idade = request.data.get('idade')
        if idade <20:
            data=request.data.copy()
            data['cor']=['Verde']
            request._full_data=data

        return super().get(request, *args, **kwargs)

#esquece isso 
class LoginView(CreateAPIView):
    serializer_class=LoginSerializer
    permission_classes=[AllowAny]

    def create(self,request,*args,**kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = serializer.validated_data['usuario']
        usuario_serializer =DonoDoPatoSerializer(usuario)

        return Response({
            'usuario':usuario_serializer.data,
            'refresh':serializer.validated_data['refresh'],
            'access':serializer.validated_data['access']
        },status=status.HTTP_200_OK)

#ja coloquei isso
class LoginView2(TokenObtainPairView):
    serializer_class=LoginSerializer2