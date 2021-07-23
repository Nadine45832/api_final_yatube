from rest_framework import permissions


class OwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        """this check for retrieve method"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
