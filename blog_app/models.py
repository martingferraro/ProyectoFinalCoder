from django.db import models

# Create your models here.

class Blog(models.Model):
    titulo= models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo= models.TextField(max_length=500)
    autor= models.CharField(max_length=50)
    fecha_creacion= models.DateField(auto_now_add=True)
    fecha_edicion= models.DateField(auto_now=True)

    # AGREGAR IMAGEN

    def __str__(self):
        return self.titulo