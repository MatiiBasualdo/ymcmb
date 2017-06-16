from django.shortcuts import render
from django.utils import timezone
from .models import Video

# Create your views here.

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'ymc/video_list.html', {'videos': videos})
