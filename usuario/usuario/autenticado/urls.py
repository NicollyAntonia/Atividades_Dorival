from django.urls import path
from .views import (
    UsuarioListCreatAPIView,
    UsuarioRetrieveUpdateDestroyAPIView,
    LoginView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('usuarios/', UsuarioListCreatAPIView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroyAPIView.as_view(), name='usuario-detail'),
]
