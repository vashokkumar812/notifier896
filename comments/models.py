from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
    name =models.CharField(max_length=255,default='')    
         
         
class comment(models.Model):
    name =models.CharField(max_length=255,default=' ')
    by =models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    of = models.ForeignKey(post, on_delete=models.CASCADE, null=True)
    def __str__(self): 
         return self.name