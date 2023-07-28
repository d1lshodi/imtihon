from rest_framework.permissions import BasePermission

class FieldPermission(BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'o':
            return True
        else:
            return True