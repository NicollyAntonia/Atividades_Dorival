from rest_framework.permissions import BasePermission

class IsHumano (BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticate and request.user.especie == 'H'
    

class IsAlien (BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticate and request.user.especie == 'A'
    
class IsExperimento (BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticate and request.user.especie == 'E'
    
class IsHumanoOuMorador(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.especie== 'H':
            return True
        return obj.planeta== request.user.planeta.id