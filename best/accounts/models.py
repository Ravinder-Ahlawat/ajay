from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class pubg_info(models.Model):
    
    pubg_id = models.CharField(max_length=9)
    pubg_username = models.CharField(max_length=20)
    