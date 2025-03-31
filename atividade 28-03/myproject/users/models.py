from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Definir related_name para resolver conflitos com o modelo User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Modificar o related_name aqui
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Modificar o related_name aqui
        blank=True
    )
