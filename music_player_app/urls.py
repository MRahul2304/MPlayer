from django.contrib.auth.views import LogoutView
from django.urls import path, include
from music_player_app.views import register, user_login, index, UpdateSong, AddSong, SongListCreateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/songs/', SongListCreateView.as_view(), name='song-list-create'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', index, name='home'),
    path('UpdateSong/<int:pk>/', UpdateSong, name='UpdateSong'),
    path('AddSong/', AddSong, name='AddSong'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)