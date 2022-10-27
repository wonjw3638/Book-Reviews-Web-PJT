from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.URLField()
    description = models.TextField()
