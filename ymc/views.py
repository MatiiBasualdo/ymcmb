from django.shortcuts import render
from django.utils import timezone
from .models import Video, Categoria

def video_list(request):
    videos = Video.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'ymc/video_list.html', {'categorias': categorias, 'videos': videos})
