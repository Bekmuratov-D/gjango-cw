# Generated by Django 4.0.5 on 2022-07-08 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0018_actor_last_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='last_names',
        ),
    ]