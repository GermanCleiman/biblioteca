""" Configuración de la URL de la biblioteca

La lista `urlpatterns` enruta las direcciones URL a las vistas. Para más información por favor vea:
     https://docs.djangoproject.com/en/2.0/topics/http/urls/
Ejemplos:
Vistas de funciones
     1. Agregar una importación: desde las vistas de importación my_app
     2. Agregue una URL a urlpatterns: ruta ('', views.home, name = 'home')
Vistas basadas en clase
     1. Agregue una importación: desde other_app.views import Inicio
     2. Agregue una URL a urlpatterns: ruta ('', Home.as_view (), name = 'home')
Incluyendo otro URLconf
     1. Importe la función include (): desde django.urls import include, path
     2. Agregue una URL a urlpatterns: ruta ('blog /', include ('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.libro.views import Inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    # especifico ('la ruta' y 'el nombre de las urls de libro')
    path('libro/', include(('apps.libro.urls', 'libro'))),
    path('', Inicio.as_view(), name = 'index')
]
