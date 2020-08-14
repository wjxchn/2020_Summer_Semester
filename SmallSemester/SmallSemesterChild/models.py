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

class Group(models.Model):
    creater = models.TextField()  #foreign
    groupid = models.IntegerField(primary_key = True , default = 0)
    time = models.DateTimeField(auto_now = True)
    group_name = models.TextField()
    introduction = models.TextField()

class Document(models.Model):
    doc_name = models.TextField()
    doc_id = models.IntegerField(primary_key = True , default = 0)
    doc_content = models.TextField()
    introduction = models.TextField()
    time = models.DateTimeField(auto_now = True)
    doc_groupid = models.IntegerField(null=True,blank=True)   #foreign
    doc_creater = models.TextField(null=True)   #foreign
    isin_recycle = models.BooleanField()

class Comment(models.Model):
    com_content = models.TextField()
    time = models.DateTimeField(auto_now = True)
    com_author = models.TextField()  #foreign
    com_id = models.IntegerField(primary_key = True , default = 0) 
    doc_id = models.IntegerField()     #foreign

class Demo(models.Model):
    demo_id = models.IntegerField(primary_key = True , default = 0) 
    demo_content = models.TextField()

class Browse(models.Model):
    browse_time = models.DateTimeField(auto_now = True)
    browse_id = models.IntegerField(primary_key = True , default = 0) 
    username = models.TextField()   #foreign
    doc_id = models.IntegerField()    #foreign

class Belong(models.Model):
    group_id = models.IntegerField()   #foreign
    username = models.TextField()   #foreign

class Favorite(models.Model):
    doc_id = models.IntegerField()      #foreign
    username = models.TextField()   #foreign

class UserExtension(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='extension')
    name = models.TextField()
    sex = models.TextField()
    selfintro = models.TextField()

@receiver(post_save,sender=User)
def create_user_extension(sender,instance,created,**kwargs):
    if created:
        UserExtension.objects.create(user=instance)
    else:
        instance.extension.save()

