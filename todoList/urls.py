from django.contrib import admin
from todolistapp import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', views.TaskViewSet,basename="tasks") 

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
     
]

    #path('auth/', include('djoser.urls.authtoken')),  