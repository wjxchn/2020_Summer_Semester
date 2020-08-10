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

class UserExtension(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='extension')
    birthday = models.DateField(null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    hassendemail = models.IntegerField(default = 0)

@receiver(post_save,sender=User)
def create_user_extension(sender,instance,created,**kwargs):
    if created:
        UserExtension.objects.create(user=instance)
    else:
        instance.extension.save()
