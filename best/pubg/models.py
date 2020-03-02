from django.db import models

# Create your models here.

class Match(models.Model):
    match_id = models.AutoField
    match_name = models.CharField(max_length=20)
    match_type = models.CharField(max_length=5)
    match_map = models.CharField(max_length=20)
    match_date = models.DateField()
    match_time = models.TimeField()
    match_entry = models.IntegerField()
    per_kill_prize = models.IntegerField()
    winner_prize = models.IntegerField()
    match_pics = models.ImageField(default='')


class Join(models.Model):
    username = models.CharField(max_length=20)
    pubg_id = models.IntegerField()
    Match_id = models.IntegerField()
    match_name = models.CharField(max_length=20)
    pubg_name = models.CharField(max_length=20)

    
class Links(models.Model):
    Heading = models.CharField(max_length=50)
    link = models.URLField()

