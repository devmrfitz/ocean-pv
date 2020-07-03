from django.db import models
from users.models import UserProfile
from django.urls import reverse

from .validators import json_validator, percentage_validator


class BaseAnswerGroup(models.Model):

    def calc_scores(self):
        return

    answer_date_and_time = models. DateTimeField(auto_now_add=True)
    self_user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='%(class)s_self')
    answers = models.TextField(
        validators=[json_validator], editable=False
    )
    accuracy = models.FloatField(
        null=True, blank=True,
        validators=[percentage_validator]
    )
    scores = models.TextField(calc_scores, editable=False)

    class Meta:
        abstract = True

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
