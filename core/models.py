from django.db import models
from django.core.validators import MaxLengthValidator
from rest_framework.validators import UniqueValidator


class SongModel(models.Model):
    song_id = models.IntegerField(unique=True,primary_key=True)
    song_name = models.CharField(blank=False,max_length=100, validators=[MaxLengthValidator])
    song_duration = models.PositiveIntegerField(blank=False)
    upload_time = models.DateTimeField(auto_now_add=True)

class PodcastModel(models.Model):
    podcast_id = models.IntegerField(unique=True, primary_key=True,blank=False)
    podcast_name = models.CharField(blank=False,max_length=100,validators=[MaxLengthValidator])
    podcast_duration = models.PositiveIntegerField(blank=False)
    upload_time = models.DateTimeField(auto_now_add=True)
    podcast_host = models.CharField(max_length=100,validators=[MaxLengthValidator], blank=False)
    podcast_participant = models.TextField(null=True, blank=True)

class AudioBookModel(models.Model):
    audiobook_id = models.IntegerField(unique=True,primary_key=True)
    audiobook_title = models.CharField(max_length=100,validators=[MaxLengthValidator], blank=False)
    title_author = models.CharField(max_length=100,validators=[MaxLengthValidator],blank=False)
    audiobook_narrator = models.CharField(max_length=100, validators=[MaxLengthValidator],blank=False)
    upload_time = models.DateTimeField(auto_now_add=True)
