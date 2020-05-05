from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)

class Song(models.Model):
    artist_id = models.ForeignKey(Artist,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    youtube_link = models.TextField('youtube link')
    date = models.DateField('date published')
