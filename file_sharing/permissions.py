from rest_framework import permissions


class IsOwnerOrPublic(permissions.BasePermission):
    """
    Custom permission to allow users to view their own files
    and public files while restricting access to private files.
    """

    def has_object_permission(self, request, view, obj):
        # Allow access to public files for all users
        if not obj.is_private:
            return True

        # Allow access to the owner of the file
        return obj.uploaded_by == request.user
