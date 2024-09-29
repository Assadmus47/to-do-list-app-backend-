from django.shortcuts import render
from django.shortcuts import render 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import viewsets, status
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.models import Group
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Client, User  
from .serializers import ClientSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,logout

# Create your views here.
