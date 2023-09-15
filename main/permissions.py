from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwner(BasePermission):
    message = "Вы не владелец"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsModer(BasePermission):
    message = "Вы не модератор"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODER:
            return True
        return False


class IsPublic(BasePermission):
    message = "Вы не моможете просматривать этот материал"

    def has_object_permission(self, request, view, obj):
        return obj.is_public
