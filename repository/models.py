from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=50, db_column='nombre_categoria')


class Recurso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    
    # Relaciones con otros modelos.
    propietario = models.ForeignKey(to=User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(
        to=Categoria, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.nombre


class RecursoImagen(Recurso):
    archivo = models.ImageField(upload_to='images')


class RecursoSonido(Recurso):
    archivo = models.FileField(upload_to='audios')
    
    
class RecursoEnlazado(Recurso):
    url = models.URLField()


class Lista(models.Model):
    TIPO_FAVORITOS = True
    TIPO_VER_MAS_TARDE = False
    
    tipo_lista = models.BooleanField(default=TIPO_VER_MAS_TARDE)
    
    # Relaciones con otros modelos.
    propietario = models.ForeignKey(to=User, on_delete=models.CASCADE)
    recursos = models.ManyToManyField(
        to = Recurso,
        db_table = 'detalle_lista'
    )
    
    def __str__(self):
        if es_favorito == True:
            return "Lista de favoritos"
        else:
            return "Lista de ver mas tarde"
