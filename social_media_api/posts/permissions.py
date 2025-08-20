from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only allow owners of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS → always allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise → only author can edit/delete
        return obj.author == request.user
