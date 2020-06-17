from django.db.models import Q

from users.models import UserProfile 


def find_similar_usernames(form):
	username = form.cleaned_data.get('username').strip().tolower()
	queryset = UserProfile.objects.filter(Q(user__username__contains=username))
	
	return queryset 