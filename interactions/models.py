from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
from django.conf import settings
from django.urls import reverse

from .validators import json_validator


class BaseAnswerGroup(models.Model):
    
    answer_date_and_time = models. DateTimeField(auto_now_add=True)
    self_user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='%(class)s_self')
    answers = models.TextField(validators=[json_validator])
    
    class Meta:
        abstract = True

class SelfAnswerGroup(BaseAnswerGroup):

    def __str__(self):
        return f"{self.id}"

    def get_absolute_url(self):
        return reverse('graphs:single_result', kwargs={'pk': self.pk})


class RelationAnswerGroup(BaseAnswerGroup):
    relation_user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='%(class)s_relation')

    def __str__(self):
        return f"{self.id}"
    