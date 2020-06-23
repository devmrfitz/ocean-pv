""" This module can be used to create random answers for the insertion into the
database for initial setup. Run
`cat docs/project_deps/data_creation/answer_creator.py | python manage.py shell
to use this. User should exist in the database first.
Remember to change USERNAME to your username. """

import random

from interactions.models import SelfAnswerGroup, UserAnswerChoice, SelfQuestion
from users.models import UserProfile

USERNAME = 'ignisda'  # Change this

for i in range(5):
    user_profile = UserProfile.objects.get(user__username=USERNAME)

    answer_group = SelfAnswerGroup.objects.create(user_profile=user_profile)
    for num in range(44):
        question = SelfQuestion.objects.get(overall_question_number=num+1)
        answer_choice = UserAnswerChoice.objects.create(
            user=user_profile.user, self_answer_group=answer_group,
            question=question, answer_choice=random.randint(1, 5)
        )
