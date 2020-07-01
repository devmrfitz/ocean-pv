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
        json_data = json.loads(answer_group.answers)
        answers = [ans['answer_choice'] for ans in json_data]
        question_factors = [ans['question']['factor'] for ans in json_data]
        qn_subclasses = [ans['question']['subclass'] for ans in json_data]

        final_scores = [answer*question_factor for answer,
                        question_factor in zip(answers, question_factors)]

        scores = [0, 0, 0, 0, 0]
        for final_score, question_subclass in zip(final_scores, qn_subclasses):
            if question_subclass == 'openness':
                scores[0] = scores[0]+final_score
            elif question_subclass == 'conscientiousness':
                scores[1] = scores[1]+final_score
            elif question_subclass == 'extraversion':
                scores[2] = scores[2]+final_score
            elif question_subclass == 'agreeableness':
                scores[3] = scores[3]+final_score
            elif question_subclass == 'neuroticism':
                scores[4] = scores[4]+final_score

        dictionary.update({'score': scores})

    return valid_dict
