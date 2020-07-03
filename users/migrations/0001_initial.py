# Generated by Django 3.0.7 on 2020-07-03 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('user_bio', models.TextField(null=True)),
                ('country', django_countries.fields.CountryField(
                    blank=True, max_length=2, null=True)),
                ('gender', models.CharField(choices=[
                 ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=140, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('special_access', 'Can access the special page'),),
            },
        ),
    ]
