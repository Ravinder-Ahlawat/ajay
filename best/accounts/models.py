from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserDetails(models.Model):
    user_id = models.IntegerField()
    phone = models.CharField(max_length=10, blank=True)
    pubg_id = models.CharField(max_length=9, blank=True)
    pubg_name = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    age = models.DateField()






class wirthdraw(models.Model):
    amount = models.CharField(max_length=3)
    paytm_no = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    