import random 

from interactions.models import SelfAnswerGroup, UserAnswerChoice, SelfQuestion
from users.models import UserProfile

for i in range(15):
	user_profile = UserProfile.objects.get(user__username='ignisda')
	
	answer_group = SelfAnswerGroup.objects.create(user_profile = user_profile)
	for num in range(44):
		question = SelfQuestion.objects.get(overall_question_number = num+1)
		answer_choice = UserAnswerChoice.objects.create(
                user = user_profile.user, self_answer_group = answer_group, question = question, answer_choice = random.randint(1,5))