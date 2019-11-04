from django.contrib import admin
from django.urls import path, include
from accounts.views import profile

urlpatterns = [
    path('profile', profile, name="profile"),
]
