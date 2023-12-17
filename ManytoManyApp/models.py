from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length = 100)
    singer_name = models.CharField(max_length = 100)
    listened = models.IntegerField()
    created_at = models.DateField()
    
class Listener(models.Model):
    account_name = models.CharField(max_length = 50)
    registration_date = models.DateField()
    songs = models.ManyToManyField(
        Song,
        related_name = 'Song',
        related_query_name = 'song'
    )