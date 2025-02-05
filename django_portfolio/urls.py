"""django_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.home),
    path('blog/', include('blog.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""        urlpatterns +=    urlpatterns es una lista en Django que contiene las rutas (URLs) que el proyecto puede manejar.
                += lo que se hace es agregar una nueva ruta (o patrón de URL) a la lista existente de URLs.

            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT):
                Esta es una llamada a la función static de Django, que sirve para servir archivos estáticos durante el desarrollo. Aunque normalmente se usa para servir archivos como imágenes, CSS o JavaScript, en este caso está configurado para servir archivos multimedia subidos por los usuarios.
            settings.MEDIA_URL:     
                Es la URL pública que será usada para acceder a los archivos multimedia desde el navegador. Esto normalmente tiene un valor como "/media/", lo que significa que los archivos subidos por los usuarios estarán accesibles en URLs que empiecen con /media/.
            settings.MEDIA_ROOT: 
                Es la ruta del sistema de archivos donde los archivos multimedia realmente se almacenan en el servidor. Generalmente, esto apunta a una carpeta dentro del proyecto, como os.path.join(BASE_DIR, 'media/'), donde BASE_DIR es el directorio raíz del proyecto.

        ¿Por qué es necesario?

            Django no sirve archivos estáticos o archivos multimedia en producción de la misma forma que en desarrollo. Durante el desarrollo (cuando se usa el servidor integrado de Django), se necesita especificar explícitamente cómo servir estos archivos.

            En este caso, esa línea permite que Django sirva los archivos en la carpeta MEDIA_ROOT a través de una URL pública definida en MEDIA_URL, como si fueran archivos estáticos, pero solo en el entorno de desarrollo.

        Ejemplo práctico:

            Supón que tienes un archivo de imagen que un usuario subió, y está guardado en la carpeta media del proyecto.
            Si la URL pública de medios es /media/ (como se configura en settings.MEDIA_URL), y el archivo está guardado en el directorio media/uploads/imagen.jpg, entonces este archivo se podrá acceder a través de la URL: http://localhost:8000/media/uploads/imagen.jpg.

  """