from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # The SAFE_METHODS are read methods. Here we are checking
        # if the user is just trying to read his own data
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise, check if the user is trying to update his own profile
        return obj.id == request.user.id
