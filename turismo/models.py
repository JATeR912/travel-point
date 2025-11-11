from django.db import models
from django.contrib.auth.models import User

class LugarTuristico(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='lugares/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre