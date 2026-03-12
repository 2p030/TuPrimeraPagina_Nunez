from django.urls import path
from .views import (
    home,
    about,
    PageListView,
    PageDetailView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),

    path("pages/", PageListView.as_view(), name="pages_list"),
    path("pages/create/", PageCreateView.as_view(), name="page_create"),
    path("pages/<int:pk>/", PageDetailView.as_view(), name="page_detail"),
    path("pages/<int:pk>/edit/", PageUpdateView.as_view(), name="page_edit"),
    path("pages/<int:pk>/delete/", PageDeleteView.as_view(), name="page_delete"),
]