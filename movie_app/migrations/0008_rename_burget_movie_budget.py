# Generated by Django 4.0.5 on 2022-07-07 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_movie_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='burget',
            new_name='budget',
        ),
    ]