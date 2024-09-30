from django.db import models
from django.contrib.auth.models import User

class Users (models.Model):
    phone_number=models.CharField(max_length=20)
    user= models.OneToOneField(User ,on_delete=models.CASCADE ,null=True, blank=True)
    


# Create your models here.
class Task(models.Model):
    utilisateur = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)         
    date_creation = models.DateTimeField(auto_now_add=True)  
    date_modification = models.DateTimeField(null=True, blank=True)
    termine = models.BooleanField(default=False)


    
