from django.db import models

# Create your models here.

class News(models.Model):
    data_index = models.IntegerField(default=-1)
    year = models.CharField(max_length=4)
    quarter = models.CharField(max_length=1)
    message = models.CharField(max_length=200)

class EventGallery(models.Model):
    data_index = models.IntegerField(default=-1)
    year = models.CharField(max_length=4)
    quarter = models.CharField(max_length=1)
    image = models.CharField(max_length=100)
    conference = models.CharField(max_length=50)

class EventGalleryDetail(models.Model):
    data_index = models.IntegerField(default=-1)
    year = models.CharField(max_length=4)
    image = models.CharField(max_length=100)
    conference = models.CharField(max_length=50)


