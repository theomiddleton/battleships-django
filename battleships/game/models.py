from django.db import models

class Highscore(models.Model):
    name = models.CharField(max_length=255)
    score = models.IntegerField()

class score(models.Model):
    name = models.CharField(max_length=255)
    score = models.IntegerField()