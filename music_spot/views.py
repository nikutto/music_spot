from django.shortcuts import render
from django.views import generic
from .models import Artist,Song
# from .models import Artist
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "music_spot/index.html"

class ArtistDetailView(generic.DetailView):
    model = Artist
    template_name = "music_spot/artist_detail.html"    

class SongDetailView(generic.DetailView):
    template_name = "music_spot/song_detail.html"
    model = Song

class SongListView(generic.ListView):
    template_name = "music_spot/song_list.html"
    model = Song
    def get_queryset(self):
        return Song.objects.order_by('name')

class ArtistListView(generic.ListView):
    template_name = "music_spot/artist_list.html"
    model = Artist
    def get_queryset(self):
        return Artist.objects.order_by('name')

class ContactView(generic.TemplateView):
    template_name = "music_spot/contact.html"


