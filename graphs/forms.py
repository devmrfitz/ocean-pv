from django import forms

from interactions.models import SelfAnswerGroup


class GraphSelector(forms.Form):
    primary_key = forms.CharField(
        required=True,
        label='Test ID',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Enter Test ID here'
            }
        )
    )
    answer_group = forms.ModelChoiceField(queryset=None, label='Your Test ID')

    def __init__(self, user, *args, **kwargs):
        super(GraphSelector, self).__init__(*args, **kwargs)
        self.fields['answer_group'].queryset = SelfAnswerGroup.objects.filter(
            self_user_profile=user.profile).order_by('-answer_date_and_time')
