from django.db import models

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100, null=True, default=None)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')
    audio_img = models.FileField(upload_to='audio_img/')

    def __str__(self):
        return self.title