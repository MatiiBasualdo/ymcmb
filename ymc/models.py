from django import forms
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    contrasena = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'contrasena': forms.PasswordInput(),
    }
    email = models.EmailField(max_length=254)
    video_asignado = models.ForeignKey('Video')

class Video(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    comentario = models.TextField()
    categoria = models.CharField(max_length=200)
    duracion = models.DurationField()
    puntaje = models.IntegerField()
    cant_clicks = models.IntegerField()
    cant_comentarios = models.IntegerField()
    publicidad_asignada = models.ForeignKey('Publicidad')

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    puntaje = models.IntegerField()

class Publicidad(models.Model):
    nombre = models.CharField(max_length=200)
    duracion = models.DurationField()
    dinero_generado = models.IntegerField()
    cant_clicks = models.IntegerField()
