from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, cat):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            if cat.user == request.user:
                print('worked')
            return cat.user == request.user
        return True


class IsNotAuthor(BasePermission):
    def has_object_permission(self, request, view, cat):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            if cat.user == request.user:
                return False
            else:
                return True
