from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    user_bio = models.TextField(null=True)
    country = CountryField(blank=True, null=True)
    gender = models.CharField(
        max_length=140,
        null=True,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        )
    )
    birth_date = models.DateField(null=True, blank=True)
    # relations = models.ManyToManyField(UserProfile)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'username': self.user.username})

    class Meta:
        permissions = (
            ('special_access', 'Can access the special page'),
        )
