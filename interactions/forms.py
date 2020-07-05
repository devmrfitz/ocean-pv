from django import forms
from django.forms import formset_factory

from .functions import return_questions
from .validators import none_choice_validator


# FIXME: The form should display the first option, ``None`` by
# default when it is presented to the user. But if the user
# submits the form with ``None`` selected, it should raise
# error, something like 'you need to select a valid option'
class AnswerChoiceForm(forms.Form):

    CHOICES = (
        # ('', None),   # FIXME: Remove option before deployment
        (1, 'Disagree strongly'),
        (2, 'Disagree a little'),
        (3, 'Neither agree nor disagree'),
        (4, 'Agree a little'),
        (5, 'Agree strongly'),

    )
    answer_choice = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'width: 270px;'}
        ),
        choices=CHOICES,
        validators=[none_choice_validator],
        required=True
    )

    def clean_answer_choice(self):
        answer_choice = self.cleaned_data.get('answer_choice')
        if not answer_choice:
            print(answer_choice)
            raise forms.ValidationError('fuck off')
        print(answer_choice)
        return answer_choice

    class Meta:
        pass


AnswerFormset = formset_factory(
    AnswerChoiceForm, extra=len(return_questions('SelfAnswerGroup'))
)


class RelationSelectorForm(forms.Form):
    username = forms.CharField()
