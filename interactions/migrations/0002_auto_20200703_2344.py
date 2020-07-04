# Generated by Django 3.0.7 on 2020-07-03 18:14

from django.db import migrations, models
import interactions.validators


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationanswergroup',
            name='accuracy',
            field=models.FloatField(blank=True, editable=False, null=True, validators=[interactions.validators.percentage_validator]),
        ),
        migrations.AlterField(
            model_name='selfanswergroup',
            name='accuracy',
            field=models.FloatField(blank=True, editable=False, null=True, validators=[interactions.validators.percentage_validator]),
        ),
    ]
