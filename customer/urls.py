from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
path('index/',views.index),

path('message/',views.message),
path("my/",views.myhtml)
]
