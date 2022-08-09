from django.contrib import admin
from django.urls import path, include

from blog_app.views import home, blogformulario

urlpatterns = [
    path('', home, name="home"),
    path('form/', blogformulario, name="form"),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
    
    
    
]