# Mini Blog Django (MVT)

Proyecto web en Django que cumple:
- Patrón MVT
- Herencia de plantillas (base.html)
- 3 modelos: Autor, Categoria, Post
- Formularios para crear Autor, Categoria y Post
- Formulario de búsqueda en BD (sobre Post)
- Proyecto listo para subir a GitHub

## Requisitos
- Python 3.10+ (recomendado)
- Django

## Instalación
```bash
python -m venv venv
# activar:
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

pip install django
python manage.py migrate
python manage.py runserver