# Generated by Django 4.2.5 on 2023-09-20 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_learner_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learner',
            name='courses',
        ),
    ]
