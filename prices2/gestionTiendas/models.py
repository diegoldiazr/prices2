from django.db import models

# Create your models here.

class Tiendas(models.Model):
    idTienda=models.AutoField(primary_key=True, db_index=True)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=300)
    imagen=models.ImageField()
    fechaAlta=models.DateTimeField(auto_now_add=True)
