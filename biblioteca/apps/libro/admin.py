from django.contrib import admin
from .models import Autor, Libro
# como models esta en esta misma carpeta solo pongo .models, sino fuera asi pongo apps.models

# Aqui registro mis modelos para verlos en Admin, despues de makemigrations, migrate
admin.site.register(Autor)
admin.site.register(Libro)
