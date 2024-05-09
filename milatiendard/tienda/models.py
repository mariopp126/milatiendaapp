# tienda/models.py

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')

class Opiniones(models.Model):
    autor = models.CharField(max_length=100)
    opinion = models.TextField()
    calificacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor} ({self.calificacion}) {self.fecha}"
