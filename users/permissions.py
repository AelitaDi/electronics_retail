from rest_framework import permissions


class IsSelf(permissions.BasePermission):
    """
    Проверяет, является ли пользователь владельцем аккаунта.
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsActiveUser(permissions.BasePermission):
    """
    Проверяет, является ли пользователь is_active.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_active


class IsStaffUser(permissions.BasePermission):
    """
    Проверяет, является ли пользователь is_staff.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff
