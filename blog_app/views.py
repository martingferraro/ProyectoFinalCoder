from django.shortcuts import render

from blog_app.forms import Blogform
from blog_app.models import Blog

# Create your views here.

def home(request):
    return render(request, "blog_app/inicio.html")

def blogformulario (request): 

    if request.method == "POST":
        form= Blogform(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            titulo= info ["titulo"]
            subtitulo= info ["subtitulo"]
            cuerpo= info ["cuerpo"]
            autor= info ["autor"]
            blog= Blog (titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor)
            blog.save()
            return render(request, "blog_app/formulario.html")

    else:
        form= Blogform()
    return render (request, "blog_app/formulario.html",{"formulario":form})
