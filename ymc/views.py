from django.shortcuts import render
from django.utils import timezone
from .models import Video, Categoria

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'ymc/video_list.html', {'videos': videos})

def categoria_list(self):
    categorias = self.nombre
    return categorias

