from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    titulo= models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo= RichTextField(max_length=500)
    autor= models.CharField(max_length=50)
    fecha_creacion= models.DateField(auto_now_add=True)
    fecha_edicion= models.DateField(auto_now=True)

    # AGREGAR IMAGEN

    def __str__(self):
        return self.titulo