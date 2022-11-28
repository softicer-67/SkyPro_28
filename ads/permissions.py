from django.http import Http404
from rest_framework import permissions
from rest_framework.permissions import BasePermission

from ads.models import User


# class AdUpdateDeletePermission(permissions.BasePermission):
#     message = 'The owner, moderator or admin can update or delete an ad.'
#
#     def has_permission(self, request, view):
#         if request.user.id == view.kwargs['pk']:
#             return True
#         elif request.user.role == User.ADMIN or request.user.role == User.MODERATOR:
#             return True
#         else:
#             return False


class Selection:
    pass


class SelectUpdatePermission(permissions.BasePermission):
    message = 'Пользователям не доступно'

    def has_permission(self, request, view):
        try:
            ob = Selection.objects.get(pk=view.kwargs['pk'])
        except Exception:   # Selection.DoesNotExist:
            raise Http404

        if ob.owner_id == request.user.id:
            return True
        return False


