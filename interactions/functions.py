from interactions.models import (
    SelfAnswerGroup,
    RelationAnswerGroup,
    UserAnswerChoice,
    SelfQuestion
)


def save_answers_to_db(
    answer_group_model,
    answer_choice_model,
    user,
    form,
    num_questions
):
    new_answer_group = answer_group_model.objects.create(user_profile=user.profile,)
    for x in range(1, num_questions+1):
        answer = answer_choice_model.objects.create(
            user=user,
            answer_choice=form.cleaned_data.get(
                f"answer_for_question_{x}"),
            question=SelfQuestion.objects.get(
                overall_question_number=x),
            self_answer_group=new_answer_group,
        )
        answer.save()

    return new_answer_group.pk
