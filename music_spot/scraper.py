from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


DEVELOPER_KEY = "AIzaSyCoxLzNc0XzYAuL_CfVSsRLs3hL2J5EK6c"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q,max_results=30):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
  

  search_response = youtube.search().list(
    q=q,
    part="id,snippet",
    maxResults=max_results,
  ).execute()

  videos = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(search_result)
      break
    
  return search_result

from .models import Song

def set_links(force_update=False):
  for song in Song.objects.all():
    artist = song.artist
    if force_update or (song.youtube_video_id is None):
      json = youtube_search(" ".join([artist.name,song.name]))
      song.youtube_video_id = json["id"]["videoId"]
      song.save()


  