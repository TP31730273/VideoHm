from email.policy import default
from operator import truediv
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
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    channel_name=models.CharField(max_length=100,null=True,default='')
    subscribers=models.IntegerField(null=True,default=0)
    following=models.IntegerField(null=True,default=0)
    catagory=models.CharField(max_length=100,null=True,default='general')
    
    class Meta:
        db_table = 'Channels'
    
    def __str__(self):
        return self.channel_name
        

class Video(models.Model):
    channel_name = models.ForeignKey(Channels, on_delete=models.CASCADE)
    Video_Title=models.CharField(max_length=100,null=True,default='')
    video=models.FileField(upload_to='media')
    thumbnail=models.FileField(upload_to='thumbnail')
    About = models.TextField(max_length=350,null=True,default='')
    Language = models.CharField(max_length=350,null=True,default='')
    cast = models.CharField(max_length=350,null=True,default='')
    category=models.CharField(max_length=150,null=True,default='')
    
    class Meta:
        db_table = 'Video'
    
    def __str__(self):
        return self.Video_Title
