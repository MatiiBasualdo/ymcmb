from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.video_list, name='video_list'),
    url(r'^$', views.categoria_list, name='categoria_list'),
]
