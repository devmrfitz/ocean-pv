import random

import pytest
from django.utils.timezone import now
from django.contrib.auth.models import User
from mixer.backend.django import mixer

from interactions.models import (
    SelfAnswerGroup,
    RelationAnswerGroup,
)


################################################
#           WRAPPER FUNCTION                #
################################################

@pytest.fixture()
def interactions_wrapper(
    create_answer_group,
    create_answer_choices,
    create_questions,
):
    """ Creates an answer_group with valid input and
    then returns it. """

    def _interactions_wrapper(user, mode):
        if mode == "self":
            answer_group = SelfAnswerGroup.objects.create(

            )
        elif mode == "relation":
            answer_group_model = RelationAnswerGroup
        else:
            raise TypeError("Only 'self' and 'relation' modes allowed")

        return answer_group.pk

    return _interactions_wrapper
