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


if __name__ == "__main__":
  q = input()
  try:
    print(youtube_search(q))
  except HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))