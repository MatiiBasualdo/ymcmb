from django.shortcuts import render
from django.utils import timezone
from .models import *

def video_list(request):
    videos = Video.objects.all()
    categorias = Categoria.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'ymc/video_list.html', {'usuarios': usuarios, 'categorias': categorias, 'videos': videos})
