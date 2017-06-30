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
    avatar = models.FileField(upload_to='avatars/%Y/%m/%d/', default=None)

    def __str__(self):
        return self.nombre

class Video(models.Model):
    usuario_asignado = models.ForeignKey('Usuario', default=None)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey('Categoria', default=None)
    duracion = models.DurationField()
    puntaje = models.IntegerField()
    cant_clicks = models.IntegerField()
    publicidad_asignada = models.ForeignKey('Publicidad')
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    autor = models.ForeignKey('Usuario', default=None)
    contenido = models.TextField()
    cant_likes = models.IntegerField()
    video_asignado = models.ForeignKey('Video', default=None)

    def __str__(self):
        return self.nombre

    def publicar(self):
        self.fecha_publicacion= timezone.now()
        self.save()

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    puntaje = models.IntegerField()

    def __str__(self):
        return self.nombre

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Publicidad(models.Model):
    nombre = models.CharField(max_length=200)
    duracion = models.DurationField()
    dinero_generado = models.IntegerField()
    cant_clicks = models.IntegerField()

    def __str__(self):
        return self.nombre

    def publish(self):
        self.published_date = timezone.now()
        self.save()

