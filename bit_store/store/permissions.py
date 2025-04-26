from rest_framework.permissions import BasePermission
from .models import Product

class HasCreatedProductPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH']:
            return Product.objects.filter(created_by=request.user).exists()
        return True