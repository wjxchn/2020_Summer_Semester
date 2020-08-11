from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
class Test(models.Model):
    name = models.CharField(max_length=20)

class Test2(models.Model):
    name = models.CharField(max_length=20)

class Test3(models.Model):
    age = models.IntegerField(null=True,blank=True)
    phonenumber = models.CharField(max_length=200,null=True,blank=True)

class Plain(models.Model):
    plainname = models.TextField()
