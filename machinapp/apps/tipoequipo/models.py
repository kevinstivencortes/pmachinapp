from django.db import models

# Create your models here.
class TipoEquipo(models.Model):
    nombre_equipo = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre_equipo