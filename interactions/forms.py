from django import forms
from django.forms import modelformset_factory

from interactions.models import (
    SelfAnswerGroup,
    SelfQuestion,
    RelationQuestion,
    UserAnswerChoice
)


class UserAnswerChoiceForm(forms.Form):
    CHOICES = (
        #(None, None),
        (1, 'Disagree strongly'),
        (2, 'Disagree a little'),
        (3, 'Neither agree nor disagree'),
        (4, 'Agree a little'),
        (5, 'Agree strongly'),
    )
    answer_for_question_1 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_2 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_3 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_4 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_5 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_6 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_7 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_8 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_9 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_10 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_11 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_12 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_13 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_14 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_15 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_16 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_17 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_18 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_19 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_20 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_21 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_22 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_23 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_24 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_25 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_26 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_27 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_28 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_29 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_30 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_31 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_32 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_33 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_34 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_35 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_36 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_37 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_38 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_39 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_40 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_41 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_42 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_43 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
    answer_for_question_44 = forms.CharField(
        widget=forms.Select(choices=CHOICES))
