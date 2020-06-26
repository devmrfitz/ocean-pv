import json
from pprint import pprint as print

from interactions.models import (
    SelfAnswerGroup,
    RelationAnswerGroup,
)
from users.models import UserProfile


def form_json_data(formset, questions: list) -> list:
    json_data = []
    for form, question in zip(formset, questions):
        valid_dict = {
            'answer_choice': int(form.cleaned_data.get('answer_choice')),
            'question': {
                'subclass': question['subclass'],
                'factor': int(question['factor'])
            }
        }
        json_data.append(valid_dict)

    json_data = json.dumps(json_data)
    return json_data


def save_self_answers_to_db(json_data: list, request) -> int:
    """ A function that takes json data (a list of dicts) and saves them to
    the database under the model of SelfAnswerGroup """
    answer_group = SelfAnswerGroup.objects.create(
        self_user_profile=request.user.profile,
        answers=json_data
    )

    return answer_group.pk


def save_relation_answers_to_db(rel: int, json_data: list, request) -> int:
    """ A function that takes json data (a list of dicts) and saves them to
    the database under the model of RelationAnswerGroup """
    rel_profile = UserProfile.objects.get(pk=rel)
    answer_group = RelationAnswerGroup.objects.create(
        self_user_profile=request.user.profile,
        answers=json_data,
        relation_user_profile=rel_profile
    )

    return answer_group.pk
