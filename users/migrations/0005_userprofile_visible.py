# Generated by Django 3.0.5 on 2020-06-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200614_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
