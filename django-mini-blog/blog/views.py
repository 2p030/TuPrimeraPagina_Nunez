from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm
from .models import Post
from django.shortcuts import get_object_or_404

def home(request):
    posts = Post.objects.order_by("-creado_en")[:10]
    return render(request, "blog/home.html", {"posts": posts})

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AutorForm()
    return render(request, "blog/autor_form.html", {"form": form})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CategoriaForm()
    return render(request, "blog/categoria_form.html", {"form": form})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})

def buscar_post(request):
    form = BuscarPostForm(request.GET or None)
    resultados = []

    if form.is_valid():
        q = form.cleaned_data.get("q", "")
        if q:
            resultados = Post.objects.filter(
                Q(titulo__icontains=q) | Q(contenido__icontains=q)
            ).order_by("-creado_en")

    return render(request, "blog/buscar.html", {
        "form": form,
        "resultados": resultados
    })

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/detalle_post.html", {"post": post})