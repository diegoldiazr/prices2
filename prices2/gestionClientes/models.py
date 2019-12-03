from django.db import models

# Create your models here.

class Clientes(models.Model):
    idCliente=models.AutoField(primary_key=True, db_index=True)
    nombre=models.CharField(max_length=100)    
    imagen=models.ImageField()
    fechaAlta=models.DateTimeField(auto_now_add=True)
