from django.urls import path, re_path
from lab8 import settings
from django.conf.urls.static import static
from . import views

app_name = "pokedex"
urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^pokemon/(?P<id>\d+)/$', views.pokemon, name="pokemon"),
    re_path(r'^trainer/(?P<id>\d+)/$', views.trainer, name="trainer"),
    re_path(r'^add_pokemon/$', views.add_pokemon, name="add_pokemon"),
    re_path(r'^edit_pokemon/(?P<pokemon_id>\d+)/$', views.edit_pokemon, name="edit_pokemon"),
    re_path(r'^delete_pokemon/(?P<pokemon_id>\d+)/$', views.delete_pokemon, name="delete_pokemon")
]       

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)