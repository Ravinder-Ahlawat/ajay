from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class pubg_info(models.Model):
    user = models.CharField(max_length=20, default='')
    pubg_id = models.CharField(max_length=9)
    pubg_username = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=10, default='')
    clan = models.CharField(max_length=20, default='')


class wirthdraw(models.Model):
    amount = models.CharField(max_length=3)
    paytm_no = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    