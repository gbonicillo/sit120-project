from rest_framework import permissions
from .models import Shop

# Check if user owns profile


class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

# Checks if user owns Shop


class IsShopOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        allowed = False
        if request.method in permissions.SAFE_METHODS:
            return True

        if hasattr(obj, "owner"):
            allowed = obj.owner.id == request.user.id

        elif hasattr(obj, "shop"):
            print("here @ shop")
            shop = Shop.objects.get(pk=obj.shop.id)
            allowed = shop.owner.id == request.user.id

        return allowed
# Check if user is of type owner


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.type == "OW"
