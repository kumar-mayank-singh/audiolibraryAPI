# Generated by Django 3.1.7 on 2021-03-28 21:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioBookModel',
            fields=[
                ('audiobook_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('audiobook_title', models.CharField(max_length=100, validators=[django.core.validators.MaxLengthValidator])),
                ('title_author', models.CharField(max_length=100, validators=[django.core.validators.MaxLengthValidator])),
                ('audiobook_narrator', models.CharField(max_length=100, validators=[django.core.validators.MaxLengthValidator])),
                ('upload_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PodcastModel',
            fields=[
                ('podcast_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('podcast_name', models.CharField(max_length=100, validators=[django.core.validators.MaxLengthValidator])),
                ('podcast_duration', models.PositiveIntegerField()),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('podcast_host', models.CharField(max_length=100, validators=[django.core.validators.MaxLengthValidator])),
                ('podcast_participant', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SongModel',
            fields=[
                ('song_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('song_name', models.CharField(max_length=100, validators=[django.core.validators.MaxLengthValidator])),
                ('song_duration', models.PositiveIntegerField()),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
