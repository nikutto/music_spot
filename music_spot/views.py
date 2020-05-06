from django.shortcuts import render
from django.views import generic
from .models import Artist,Song
# from .models import Artist
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "music_spot/index.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["artist_list"] = Artist.objects.all()
        return context

class DetailView(generic.DetailView):
    model = Artist
    template_name = "music_spot/detail.html"

