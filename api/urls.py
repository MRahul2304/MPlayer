from django.urls import path
from .views import SongListCreateView, SongDetailView

urlpatterns = [
    path(' ', SongListCreateView.as_view(), name='song-list-create'),
    path('songs/&lt;int:pk&gt;/', SongDetailView.as_view(), name='song-detail'),
]