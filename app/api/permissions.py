from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    """
    Everyone can view.
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsUserOrStaff(BasePermission):
    """
    Private data only visible to user and staff.
    """
    def has_object_permission(self, request, view, obj):
        if obj.customer.user == request.user or request.user.is_staff:
            return True
        else:
            return False


class IsUserOrStaffOrReadOnly(BasePermission):
    """
    Everyone can view, user and staff can edit.
    """
    def has_object_permission(self, request, view, obj):
        """
        GET, HEAD or OPTIONS requests always allowed.
        """
        if request.method in SAFE_METHODS:
            return True

        """
        Write permissions user and staff only
        """
        if obj.customer.user == request.user or request.user.is_staff:
            return True
        else:
            return False


class IsStaffOrReadOnly(BasePermission):
    """
    Everyone can view, staff can edit.
    """
    def has_object_permission(self, request, view, obj):
        """
        GET, HEAD or OPTIONS requests always allowed.
        """
        if request.method in SAFE_METHODS:
            return True

        """
        Write permissions staff only
        """
        return request.user.is_staff


class IsUser(BasePermission):
    """
    Private user data.
    """
    message = 'This information is private.'
    def has_object_permission(self, request, view, obj):
        return obj.customer.user == request.user
