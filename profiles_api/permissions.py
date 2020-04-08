from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # 1: The SAFE_METHODS are read methods. Here we are checking
        # if the user is just trying to read his own data
        # 2: Apparently the create method is also a safe methog
        # Only the methods that alter and delete existing data are not
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise, check if the user is trying to update his own profile
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
