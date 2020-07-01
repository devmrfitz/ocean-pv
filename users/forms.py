from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django_countries.widgets import CountrySelectWidget

from users.models import UserProfile
from mixins import RequiredFieldsMixin


class RegistrationForm(RequiredFieldsMixin, UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        required_fields = '__all__'

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)

            if commit:
                user.save()

            return user


class ProfileUpdateForm(RequiredFieldsMixin, forms.ModelForm):

    user_bio = forms.CharField(widget=forms.Textarea(
        attrs={'style': 'height: 200px'})
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    visible = forms.ChoiceField(
        choices=CHOICES,
        help_text='Whether your profile will be publicly visible or not'
    )

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'country': CountrySelectWidget(
                layout='{widget}'
            ),
        }
        required_fields = '__all__'


class UserUpdateForm(RequiredFieldsMixin, forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        required_fields = '__all__'
