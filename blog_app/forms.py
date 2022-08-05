from django import forms

class Blogform(forms.Form):
    titulo= forms.CharField(max_length=50)
    subtitulo= forms.CharField(max_length=50)
    cuerpo= forms.CharField(max_length=500)
    autor= forms.CharField(max_length=50)
