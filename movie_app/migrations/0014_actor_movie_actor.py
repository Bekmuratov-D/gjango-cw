# Generated by Django 4.0.5 on 2022-07-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0013_movie_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('М', 'Мужчина'), ('Ж', 'Женщина')], default='М', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(to='movie_app.actor'),
        ),
    ]
