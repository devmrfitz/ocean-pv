from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
from django.conf import settings
from django.urls import reverse

CHOICES = (
    (1, 'Disagree strongly'),
    (2, 'Disagree a little'),
    (3, 'Neither agree nor disagree'),
    (4, 'Agree a little'),
    (5, 'Agree strongly')
)

SUBCLASS_CHOICES = (
    ('openess', 'openess'),
    ('conscientiousness', 'conscientiousness'),
    ('extraversion', 'extraversion'),
    ('agreeableness', 'agreeableness'),
    ('neuroticism', 'neuroticism')
)


class SelfQuestion(models.Model):
    overall_question_number = models.IntegerField()
    question_text = models.TextField()
    ocean_subclass = models.CharField(max_length=150, choices=SUBCLASS_CHOICES)
    question_factor = models.IntegerField(choices=(
        (-1, 'negative'),
        (1, 'positive')
    ))

    def __str__(self):
        return f"Question {self.overall_question_number}: {self.question_text}"


class SelfAnswerGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_date_and_time = models. DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s answer group, {self.id}"

    def get_absolute_url(self):
        return reverse('graphs:single_result', kwargs={'pk': self.pk})


class UserAnswerChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_choice = models.IntegerField(choices=CHOICES)
    question = models.ForeignKey(SelfQuestion, on_delete=models.CASCADE)
    self_answer_group = models.ForeignKey(
        SelfAnswerGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s answer choices"


class Average(models.Model):
    associated_date = models.DateField(auto_now=True)
    global_poll_average = models.FloatField()  # user specific
    question = models.ForeignKey(SelfQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Average for {self.associated_date}"


class RelationQuestion(models.Model):
    overall_question_number = models.IntegerField()
    question_text = models.TextField()
    ocean_subclass = models.CharField(max_length=150, choices=SUBCLASS_CHOICES)
    question_factor = models.IntegerField(choices=(
        (-1, 'negative'),
        (1, 'positive')
    ))

    def __str__(self):
        return f"Question {self.overall_question_number}: {self.question_text}"


class RelationAnswerGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_date_and_time = models. DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s answer group, {self.id}"

    def get_absolute_url(self):
        return reverse('graphs:single_result', kwargs={'pk': self.pk})


class RelationAnswerChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_choice = models.IntegerField(choices=CHOICES)
    question = models.ForeignKey(SelfQuestion, on_delete=models.CASCADE)
    self_answer_group = models.ForeignKey(
        RelationAnswerGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s answer choices"
