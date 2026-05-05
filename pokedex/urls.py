from django.urls import path, re_path
from lab8 import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^pokemon/(?P<id>\d+)/$', views.pokemon, name="pokemon"),
    re_path(r'^trainer/(?P<id>\d+)/$', views.trainer, name="trainer"),
]       

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)