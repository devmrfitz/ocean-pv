# Generated by Django 3.0.7 on 2020-07-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0002_auto_20200703_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalAverages',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
