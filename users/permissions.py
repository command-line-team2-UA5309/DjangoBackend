from rest_framework.permissions import BasePermission

class IsGolden(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'golden'

class IsSilver(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['silver', 'golden']

class IsRegular(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['regular', 'silver', 'golden']