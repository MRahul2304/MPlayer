from django.contrib.auth.models import AbstractUser
from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    duration = models.DurationField()  # Make sure the format is correct
    file = models.FileField(upload_to='songs/')  # Ensure this is set up correctly


    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='user'
    )


