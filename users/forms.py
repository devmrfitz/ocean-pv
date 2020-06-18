from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django_countries.widgets import CountrySelectWidget

from users.models import UserProfile


class RegistrationForm(UserCreationForm):

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

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)

            if commit:
                user.save()

            return user


class ProfileUpdateForm(forms.ModelForm):

    user_bio = forms.CharField(required=False, widget=forms.Textarea)
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'country': CountrySelectWidget(
                layout='{widget}'
            ),
        }
        help_texts = {
            'visible': 'Whether your profile will be publicly visible or not'
        }


class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
