from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow staff users to edit objects.
    Other users can only view.
    """

    def has_permission(self, request, view):
        # Allow any user to read (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow staff users to perform any action
        return request.user.is_staff
