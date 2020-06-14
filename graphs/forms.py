from django import forms


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
