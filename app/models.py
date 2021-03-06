from doctest import master
from email.policy import default
from operator import truediv
from pickle import TRUE
from pyexpat import model
from django.db import models

# Create your models here.

# Create your models here.
class Master(models.Model):
    mobile_no=models.CharField(max_length=18,unique=True)
    Email=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=18)

    class Meta:
        db_table= 'master'
    
    def __str__(self):
        return self.Email

class Profile(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=30,null=True,default='')
    Mobile = models.CharField(max_length=30,null=True,default='')
    Country = models.CharField(max_length=10,null=True,default='')
    City = models.CharField(max_length=25,null=True,default='')
    Address = models.TextField(max_length=150,null=True,default='')
    Zip = models.TextField(max_length=150,null=True,default='')
    

    class Meta:
        db_table = 'profile'
    
    def __str__(self):
        return self.FullName



        # chabbel model
class Channels(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    channel_name=models.CharField(max_length=100,unique=TRUE,null=True,default='')
    subscribers=models.IntegerField(null=True,default=0)
    following=models.IntegerField(null=True,default=0)
    catagory=models.CharField(max_length=100,null=True,default='general')
    Channel_pic=models.FileField(upload_to='channel_pic')
    
    class Meta:
        db_table = 'Channels'
    
    def __str__(self):
        return self.channel_name
        

class Video(models.Model):
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE)
    Video_Title=models.CharField(max_length=100,null=True,default='')
    video=models.FileField(upload_to='videos')
    thumbnail=models.FileField(upload_to='thumbnail')
    About = models.TextField(max_length=350,null=True,default='')
    Language = models.CharField(max_length=350,null=True,default='')
    cast = models.CharField(max_length=350,null=True,default='')
    category=models.CharField(max_length=150,null=True,default='')
    
    class Meta:
        db_table = 'Video'
    
    def __str__(self):
        return self.Video_Title

class Subscriptions(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subscribed_channel = models.ForeignKey(Channels, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Subsciption'
    
    def __str__(self):
        return self.subscribed_channel.channel_name

class comments_and_likes(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    channel=models.ForeignKey(Channels, on_delete=models.CASCADE,null=True)
    comments=models.TextField(blank = True)

    class Meta:
        db_table = 'Comments_and_likes'
    
    def __str__(self):
        return self.video.Video_Title
