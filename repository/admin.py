from django.contrib import admin

from .models import RecursoImagen, RecursoSonido, RecursoEnlazado, Categoria

admin.site.register(RecursoImagen)
admin.site.register(RecursoSonido)
admin.site.register(RecursoEnlazado)
admin.site.register(Categoria)
