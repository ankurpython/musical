from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class MusicalMetadata(models.Model):
    title = models.CharField(max_length=250)
    contributors = ArrayField(models.TextField(max_length=50))
    iswc = models.CharField(unique=True, max_length=50)
