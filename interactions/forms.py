from django import forms
from django.forms import formset_factory

from .functions import return_questions
from .validators import json_validator


class AnswerChoiceForm(forms.Form):

    CHOICES = (
        # ('None', None),   # FIXME: Remove option before deployment
        (1, 'Disagree strongly'),
        (2, 'Disagree a little'),
        (3, 'Neither agree nor disagree'),
        (4, 'Agree a little'),
        (5, 'Agree strongly'),

    )
    answer_choice = forms.CharField(
        widget=forms.Select(
            choices=CHOICES,
            attrs={'class': 'form-control', 'style': 'width: 270px;'}
        ),
        required=True,
    )

    class Meta:
        fields = ['self_user_profile']


AnswerFormset = formset_factory(
    AnswerChoiceForm, extra=len(return_questions('SelfAnswerGroup'))
)


class RelationSelectorForm(forms.Form):
    username = forms.CharField()
