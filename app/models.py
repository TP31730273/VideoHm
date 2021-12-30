from django.db import models

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
    # Gender = models.CharField(max_length=10,null=True,choices=choice_gender)
    Country = models.CharField(max_length=10,null=True,default='')
    State = models.CharField(max_length=25,null=True,default='')
    City = models.CharField(max_length=25,null=True,default='')
    Address = models.TextField(max_length=150,null=True,default='')

    class Meta:
        db_table = 'profile'
    
    def __str__(self):
        return self.FullName