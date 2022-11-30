from django.http import Http404
from rest_framework import permissions

from ads.models import Selection


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


