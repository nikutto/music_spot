from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    youtube_video_id = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.name

    def youtube_link(self):
        return f"https://www.youtube.com/watch?v={self.youtube_video_id}"

    def youtube_embedded_link(self):
        return f"https://www.youtube.com/embed/{self.youtube_video_id}"
