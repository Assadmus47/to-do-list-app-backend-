from django.shortcuts import render 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import viewsets, status
from .models import *
from .serializers import *
""" api_view()
def afficher_taches(request):
    taches = Task.objects.all() 
    return Response({'taches': taches},status=200)  
 """
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  
    serializer_class = TaskSerializer
