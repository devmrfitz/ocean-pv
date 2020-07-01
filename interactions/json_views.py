from django.http import JsonResponse
from django.db.models import Q
from django.core import serializers

from users.models import UserProfile


def howto_relation_ajax(request):
    if request.is_ajax():
        username = request.GET.get('username', None)
        usernames = UserProfile.objects.filter(
            Q(user__username__contains=username)
        ).exclude(
            Q(user__username__exact=request.user.username) | Q(visible=False)
        )
        data = {
            'usernames': serializers.serialize('json', usernames)
        }
        if data['usernames']:
            data['exists'] = True
        return JsonResponse(data)
