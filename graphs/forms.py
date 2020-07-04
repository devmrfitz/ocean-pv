from django import forms

from interactions.models import SelfAnswerGroup
from interactions.validators import percentage_validator

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


class AccuracySetterForm(forms.Form):
    accuracy = forms.FloatField(widget=forms.NumberInput(
    attrs={'class':'form-control'}
    ), help_text=('Are these descriptions of you accurate?' ' Enter a percentage (0-100), 0 being "very inaccurate" and 100' ' being "extremely accurate".'), 
    validators = [percentage_validator]
    )
    pk = forms.CharField(widget=forms.HiddenInput())
    
    def form_valid(self):
    	super().form_valid()
    	if not 0<=self.accuracy<=100:
    		raise ValidationError('Number between 0 and 100 allowed')
