from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Page


def home(request):
    return render(request, "blog/home.html")


def about(request):
    return render(request, "blog/about.html")


class PageListView(ListView):
    model = Page
    template_name = "blog/pages_list.html"
    context_object_name = "pages"
    ordering = ["-id"]


class PageDetailView(DetailView):
    model = Page
    template_name = "blog/page_detail.html"


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ["titulo", "subtitulo", "contenido", "imagen", "fecha"]
    template_name = "blog/page_form.html"
    success_url = reverse_lazy("pages_list")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ["titulo", "subtitulo", "contenido", "imagen", "fecha"]
    template_name = "blog/page_form.html"
    success_url = reverse_lazy("pages_list")


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "blog/page_delete.html"
    success_url = reverse_lazy("pages_list")