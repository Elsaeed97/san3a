from rest_framework import permissions


class IsTutorialOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # check for action if create return True
        if request.method == "POST" and not obj:
            return True
        # update, delete
        return request.user.id == obj.author.id
