
from django.shortcuts import render


from blog_app.forms import Blogform, UserRegisterForm, UserCreationForm
from blog_app.models import Blog
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views import *
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
            return render(request, "blog_app/form.html")

    else:
        form= Blogform()
    return render (request, "blog_app/form.html",{"formulario":form})


def login_request(request):

    if request.method=="POST":
    
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            usu= request.POST ["username"]
            clave= request.POST ["clave"]

            usuario= authenticate(username=usu, password=clave)

            if usuario is not None: 
                login (request, usuario)
                return render (request, "blog_app/inicio.html", {'form':form, 'mensaje': f"Bienvenido {usuario}"})
            else:
                return render(request, "blog_app/login.html", {'form':form, 'mensaje': "Usuario o clave incorrectas"})

        else:
                return render(request, "blog_app/login.html", {'form':form, 'mensaje': "Usuario o clave inválidos"})

    else:
        form= AuthenticationForm()
        return render(request, "blog_app/login.html", {'form':form,})

def register(request):
    if request.method == 'POST':

             
        form = UserRegisterForm(request.POST)
        if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                return render(request,"blog_app/inicio.html" ,  {"mensaje":"Usuario Creado :)"})


    else:
                 
        form = UserRegisterForm()     

    return render(request,"blog_app/register.html" ,  {"form":form})
