from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^$', views.video_list, name='video_list'),
]
