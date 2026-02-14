from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("autor/nuevo/", views.crear_autor, name="crear_autor"),
    path("categoria/nueva/", views.crear_categoria, name="crear_categoria"),
    path("post/nuevo/", views.crear_post, name="crear_post"),
    path("buscar/", views.buscar_post, name="buscar_post"),
]