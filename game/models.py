from django.db import models

class Highscore(models.Model):
    name = models.CharField(max_length=255)
    score = models.IntegerField()
    
class Score(models.Model):
    name = models.CharField(max_length=255)
    score = models.IntegerField()