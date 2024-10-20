from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ('id','title','categorie', 'artist', )
    search_fields = ('title', 'artist')

admin.site.register(Song, SongAdmin)
