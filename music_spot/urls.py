from django.urls import path

from . import views

app_name = 'music_spot'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.ArtistDetailView.as_view(),name='artist_detail'),
    path('song/<int:pk>',views.SongDetailView.as_view(),name='song_detail'),
]