# inhirt from base permission class in django
from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """ check user can edit the profile"""


        # use safe http method (get) which is you can only retieve data and not allowed to modify , add or delete
        if request.method in permissions.SAFE_METHODS:
            return True

        # make comparison using id and if has authentication , return (is user obj id = authentication id it return true
        return obj.id == request.user.id