from rest_framework.permissions import BasePermission


class IsCustomerOrStaff(BasePermission):
    """
    Custom permission to only allow customers that
    created orders/wishlist-items to edit them.
    """

    # message = 'This post does not belong to you'
    def has_object_permission(self, request, view, obj):
        return obj.customer.user == request.user # or request.user.is_staff


    """def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user"""
