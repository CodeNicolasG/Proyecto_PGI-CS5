from django.db import models

# Create your models here.

class Miembro(models.Model):
    nombre_completo = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    legajo_personal = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    email_institucional = models.EmailField(unique=True)
    email_personal = models.EmailField()
    
    