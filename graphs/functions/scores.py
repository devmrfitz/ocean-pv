import json

from interactions.models import (
    SelfAnswerGroup,
)


def update_dict_with_score(valid_dict: list) -> list:
    """ Updates the dict (from single and multiple_result_view) with
    the scores of each user present in the list, by calculating their
    ``answer_choice`` and multiplying them with corresponding
    question factors. """

    for dictionary in valid_dict:
        answer_group = SelfAnswerGroup.objects.get(
            pk=dictionary['answer_group_pk']
        )
        scores = json.loads(answer_group.scores)
        dictionary.update({'score': scores})

    return valid_dict
