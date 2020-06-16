from functools import wraps

from interactions.models import (
    SelfAnswerGroup,
    RelationAnswerGroup,
    UserAnswerChoice,
    RelationAnswerChoice,
    SelfQuestion,
    RelationQuestion
)


def wrapper_save_answers(func):

    @wraps
    def wrapped_answers(*args, **kwargs):
        for num in range(1, kwargs['num_questions']+1):
            answer = kwargs['answer_choice_model'].objects.create(
                user=kwargs['user'],
                answer_choice=kwargs['form'].cleaned_data.get(
                    f"answer_for_question_{num}"),
                question=kwargs['question_model'].objects.get(
                    overall_question_number=num),
                self_answer_group=kwargs['new_answer_group'],
            )

        return new_answer_group.pk

    return wrapped_save_answers
