from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(models.Model):
    artist_id = models.ForeignKey(Artist,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    youtube_link = models.TextField('youtube link')
    date = models.DateField('date published')

    def __str__(self):
        return self.name
