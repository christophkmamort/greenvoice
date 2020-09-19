from rest_framework.permissions import BasePermission


class IsStaffOrReadOnly(BasePermission):
    """
    Only allow staff to edit, everyone can view.
    """

    def has_object_permission(self, request, view, obj):
        """
        Read permissions are allowed to any request,
        so we'll always allow GET, HEAD or OPTIONS requests.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        """
        Write permissions are only allowed to staff.
        """
        return request.user.is_staff


class IsUser(BasePermission):
    """
    Private user data.
    """

    message = 'This information is private.'
    def has_object_permission(self, request, view, obj):
        return obj.customer.user == request.user
