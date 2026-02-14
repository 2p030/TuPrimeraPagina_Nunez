from django import forms
from .models import Autor, Categoria, Post

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "email"]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "autor", "categoria"]

class BuscarPostForm(forms.Form):
    q = forms.CharField(label="Buscar", max_length=120, required=False)