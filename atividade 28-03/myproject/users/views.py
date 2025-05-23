from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
