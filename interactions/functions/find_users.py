from django.db.models import Q

from users.models import UserProfile
from interactions.models import SelfAnswerGroup 


def find_similar_usernames(form):
    username = form.cleaned_data.get('username').strip().lower()
    queryset = UserProfile.objects.filter(Q(user__username__contains=username))

    return queryset


def find_answer_groups_counts(queryset):
    answer_groups=[SelfAnswerGroup.objects.filter(Q(user_profile__exact=profile)).count() for profile in queryset]
    
    return answer_groups
