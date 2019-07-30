from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class blog(models.Model):
    TYPE_CHOICES=[
        ('advice','Advice'),
        ('story','Story'),
        (None,'Choose')
        ]

    title=models.CharField(max_length=100)
    Type=models.CharField(max_length=6,choices=TYPE_CHOICES)
    content=models.TextField()
    publication_date=models.DateField(auto_now_add=True)
    readers=models.CharField(max_length=10,default='0')
    country=models.CharField(max_length=50,default='none')
    picture = models.ImageField(upload_to='blogPics')
    
    def __str__(self):
        return self.title


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=20)
    GENDER_CHOICES=[
        ('Female','Female'),
        ('Male','Male'),
        (None,'Choose')
        ]
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES)

    def __str__(self):
        return self.user.username
