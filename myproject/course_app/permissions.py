from rest_framework.permissions import BasePermission



class CreateCoursePermission(BasePermission):
    def has_permission(self, request, view):
       if request.user.role == 'teacher':
           return True
       else:
           return False

class CreateExamPermission(BasePermission):
    def has_permission(self, request, view):
       if request.user.role == 'teacher':
           return True
       else:
           return False


class CheckPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'student':
            return True
        else:
            return False