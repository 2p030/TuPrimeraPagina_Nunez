from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import Page
from messaging.models import Message


def home(request):
    latest_pages = Page.objects.order_by("-id")[:3]

    context = {
        "latest_pages": latest_pages,
        "pages_count": Page.objects.count(),
        "users_count": User.objects.count(),
        "messages_count": Message.objects.count(),
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")


class PageListView(ListView):
    model = Page
    template_name = "blog/pages_list.html"
    context_object_name = "pages"
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Page.objects.filter(titulo__icontains=query).order_by("-id")
        return Page.objects.order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


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