import json

from django.db import models
from users.models import UserProfile
from django.urls import reverse

from .validators import json_validator, percentage_validator


class BaseAnswerGroup(models.Model):

    answer_date_and_time = models. DateTimeField(auto_now_add=True)
    self_user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='%(class)s_self')
    answers = models.TextField(
        validators=[json_validator], editable=False
    )
    accuracy = models.FloatField(
        null=True, blank=True,
        validators=[percentage_validator],
        editable=False
    )
    scores = models.TextField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        json_data = json.loads(self.answers)
        answers = [ans['answer_choice'] for ans in json_data]
        question_factors = [ans['question']['factor'] for ans in json_data]
        qn_subclasses = [ans['question']['subclass'] for ans in json_data]

        final_scores = [answer*question_factor for answer,
                        question_factor in zip(answers, question_factors)]

        scores = {'openness': 0, 'conscientiousness': 0, 'extraversion': 0,
                  'agreeableness': 0, 'neuroticism': 0}
        for final_score, question_subclass in zip(final_scores, qn_subclasses):
            if question_subclass == 'openness':
                scores['openness'] = (
                    scores['openness']
                    + final_score
                )
            elif question_subclass == 'conscientiousness':
                scores['conscientiousness'] = (
                    scores['conscientiousness']
                    + final_score
                )
            elif question_subclass == 'extraversion':
                scores['extraversion'] = (
                    scores['extraversion']
                    + final_score
                )
            elif question_subclass == 'agreeableness':
                scores['agreeableness'] = (
                    scores['agreeableness']
                    + final_score
                )
            elif question_subclass == 'neuroticism':
                scores['neuroticism'] = (
                    scores['neuroticism']
                    + final_score
                )
        self.scores = json.dumps(scores)
        super().save(*args, **kwargs)

    def return_formatted_json(self):
        import json
        json_data = json.loads(self.answers)
        return json.dumps(json_data, indent=4, sort_keys=True)

    return_formatted_json.short_description = 'Formatted data'


class SelfAnswerGroup(BaseAnswerGroup):

    def __str__(self):
        return f"{self.id}"

    def get_absolute_url(self):
        return reverse('graphs:single_result', kwargs={'pk': self.pk})


class RelationAnswerGroup(BaseAnswerGroup):
    relation_user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE,
        related_name='%(class)s_relation'
    )

    def __str__(self):
        return f"{self.id}"
