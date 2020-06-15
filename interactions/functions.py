from .models import (
    SelfAnswerGroup,
    RelationAnswerGroup,
    UserAnswerChoice,
    RelationAnswerChoice, 
    SelfQuestion, 
    RelationQuestion 
)
from users.models import UserProfile 


def save_self_answers_to_db(
    user,
    form,
    num_questions
):
    new_answer_group = SelfAnswerGroup.objects.create(user_profile=user.profile,)
    for x in range(1, num_questions+1):
        answer = UserAnswerChoice.objects.create(
            user=user,
            answer_choice=form.cleaned_data.get(
                f"answer_for_question_{x}"),
            question=SelfQuestion.objects.get(
                overall_question_number=x),
            self_answer_group=new_answer_group,
        )
        answer.save()

    return new_answer_group.pk

def save_relation_answers_to_db(
    user,
    relation,
    form,
    num_questions
):
    relation_profile=UserProfile.objects.get(pk=relation)
    new_answer_group = RelationAnswerGroup.objects.create(self_user_profile=user.profile, relation_user_profile=relation_profile)
    for x in range(1, num_questions+1):
        answer = RelationAnswerChoice.objects.create(
            user=user,
            answer_choice=form.cleaned_data.get(
                f"answer_for_question_{x}"),
            question=RelationQuestion.objects.get(
                overall_question_number=x),
            self_answer_group=new_answer_group,
        )
        answer.save()

    return new_answer_group.pk 