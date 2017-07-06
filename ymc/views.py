from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from django.shortcuts import render
from django.utils import timezone
from .models import *

def video_list(request):
    videos = Video.objects.all()
    categorias = Categoria.objects.all()
    usuarios = User.objects.all()
    return render(request, 'ymc/video_list.html', {'usuarios': usuarios, 'categorias': categorias, 'videos': videos})

def list(request):
    # Maneja la subida de archivos
    if request.method == 'POST':
        formulario = VideoFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            nuevo_archivo = Video(archivo = request.FILES['archivo'])
            nuevo_archivo.save()

            # Redirecciona a la lista de videos despues del POST
            return HttpResponseRedirect(reverse('ymc.views.list'))
    else:
        formulario = VideoFormulario() # Un formulario vacio, inutil

    # Cargar los videos a la lista
    videos = Video.objects.all()

    # Render list page with the documents and the form
    return render(request,
        'video_upload/list.html',
        {'videos': videos, 'formulario': formulario})
