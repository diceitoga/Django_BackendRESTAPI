from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    '''
    allow user to post their own status (not profile as above)
    '''
    def has_object_permission(self, request, view, obj):
        '''
        Checks that the user is trying to update the status
        '''
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
        '''This means if the user is same as the requester'''
