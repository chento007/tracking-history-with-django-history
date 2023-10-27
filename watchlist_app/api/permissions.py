from rest_framework import permissions

"""
    if user admin return true 
    if user not admin return false
    =============================
    this class is for custome permissions
"""

class AdminOrReadOnly(permissions.IsAdminUser): 

    """
        all access only to admin users
        - defined read and write to admin users
        - defined read only for non-admin users
    """
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or admin_permission

"""
    if user review user can acess read write
    if user normaly can read only
"""

class ReviewUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # check permissions for read only reqests GET method
        if request.method in permissions.SAFE_METHODS:
            return True        
        else :
        # check permission for write reqests
            return obj.review_user == request.user