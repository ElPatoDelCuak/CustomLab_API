from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Permite acceso solo a usuarios con el rol 'admin'.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.rol == 'admin')

class IsManager(permissions.BasePermission):
    """
    Permite acceso solo a usuarios con el rol 'manager'.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.rol == 'manager')

class IsAdminOrManager(permissions.BasePermission):
    """
    Permite acceso a usuarios con el rol 'admin' o 'manager'.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.rol in ['admin', 'manager']
        )

class IsCliente(permissions.BasePermission):
    """
    Permite acceso solo a usuarios con el rol 'cliente'.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.rol == 'cliente')
