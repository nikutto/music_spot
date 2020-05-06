from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    youtube_link = models.TextField('youtube link',blank=True)
    youtube_embedded_link = models.TextField('embedded link',blank=True)
    date = models.DateField('date published',blank=True)

    def __str__(self):
        return self.name
