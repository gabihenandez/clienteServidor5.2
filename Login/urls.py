from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from django.conf.urls import include, url
from rest_framework_swagger.views import get_swagger_view

from Login.views import CustomAuthToken

urlpatterns = [
    re_path(r'^',CustomAuthToken.as_view()),
    
]