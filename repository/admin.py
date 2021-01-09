from django.contrib import admin

from .models import RecursoImagen, RecursoSonido, RecursoEnlazado, Categoria
# Register your models here.

admin.site.register(RecursoImagen)
admin.site.register(RecursoSonido)
admin.site.register(RecursoEnlazado)
admin.site.register(Categoria)
