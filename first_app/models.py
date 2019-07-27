from django.db import models

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
    def __str__(self):
        return self.title