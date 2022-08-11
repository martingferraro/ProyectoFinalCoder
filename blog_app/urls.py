from django.contrib import admin
from django.urls import path, include

from blog_app.views import home, blogformulario, login_request, register
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', home, name="home"),
    path('blogformulario/', blogformulario, name="blogformulario"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('login/', login_request, name= 'login'),
    path('register/', register, name= 'register'),
    path('logout/', LogoutView.as_view(template_name='blog_app/logout.html'), name= 'logout'),
    
    
    
]