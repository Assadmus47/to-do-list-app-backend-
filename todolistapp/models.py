from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)         
    date_creation = models.DateTimeField(auto_now_add=True)  
    date_modification = models.DateTimeField(null=True, blank=True)
    termine = models.BooleanField(default=False)


    
