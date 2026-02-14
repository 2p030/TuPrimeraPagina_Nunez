from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=120)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo