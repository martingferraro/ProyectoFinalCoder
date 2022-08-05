from django.contrib import admin
from django.urls import path

from blog_app.views import home, blogformulario

urlpatterns = [
    path('home/', home, name="home"),
    path('form/', blogformulario, name="form"),
    
]