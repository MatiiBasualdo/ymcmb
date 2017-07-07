from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^$', views.video_list, name='video_list'),
    url(r'^list/$', views.list, name='list'),
    url(r'^categoria/(?P<cat>[0-9]+)/$', views.categoria_list, name="ymc.views.video_categoria"),
]
