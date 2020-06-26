import random

import pytest
from django.utils.timezone import now
from django.contrib.auth.models import User
from mixer.backend.django import mixer

from interactions.models import (
    SelfAnswerGroup,
    UserAnswerChoice,
    RelationAnswerGroup,
    RelationAnswerChoice
)


@pytest.fixture()
def create_answer_group():
    """ Create self answer group data for graph calculations. """
    
    def _create_answer_group(user, answer_group_model):
        answer_group = answer_group_model.objects.create(
            answer_date_and_time=now(),
            user_profile=user.profile
        )
        return answer_group

    return _create_answer_group


@pytest.fixture()
def create_questions():
    """ Create self questions in the database for graph calculations. """
    
    def _create_questions(question_model):
        return mixer.blend(f"interactions.{question_model}")

    return _create_questions


@pytest.fixture()
def create_answer_choices():
    """ Create self answer choices for graph calculations. """
    
    def _create_answer_choices(user, question, answer_group, answer_choice_model):
        return answer_choice_model.objects.create(
            user=user,
            answer_choice=random.randint(1, 5),
            question=question,
            self_answer_group=answer_group
        )

    return _create_answer_choices


################################################
#           WRAPPER FUNCTION                #
################################################

@pytest.fixture()
def interactions_wrapper(
    create_answer_group,
    create_answer_choices,
    create_questions,
):
    """ Creates an answer_group, then a question_list, then
    appropriate answer_choices and then returns them. """
    
    def _interactions_wrapper(user, mode):
        if mode == "self":
            answer_group_model = SelfAnswerGroup
            question_model = 'SelfQuestion'
            answer_choice_model = UserAnswerChoice
        elif mode == "relation":
            answer_group_model = RelationAnswerGroup
            question_model = 'RelationQuestion'
            answer_choice_model = RelationAnswerChoice
        else:
            raise TypeError("Only 'self' and 'relation' modes allowed")
        answer_group = create_answer_group(user, answer_group_model)
        for num in range(44):
            question = create_questions(question_model)
            answer_choice = create_answer_choices(
                user, question, answer_group, answer_choice_model)

        return answer_group.pk

    return _interactions_wrapper
