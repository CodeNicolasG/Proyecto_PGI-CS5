from django.db import models

class Miembro(models.Model):
    name = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    legajo = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    birth_date = models.DateField()
    ciudadania = models.CharField(max_length=100, choices=[
        ('Argentina', 'Argentina'),
        ('Brasil', 'Brasil'),
        ('Chile', 'Chile'),
        ('Paraguay', 'Paraguay'),
        ('Uruguay', 'Uruguay'),
        ('Otro', 'Otro'),
    ], default='Argentina')
    provincia_de_nacimiento = models.CharField(max_length=100, blank=True, null=True)
    ciudad_de_nacimiento = models.CharField(max_length=100, blank=True, null=True)
    email_institucional = models.EmailField(unique=True)
    email_personal = models.EmailField(blank=True, null=True)
    phone_personal = models.CharField(max_length=25)
    phone_emergency = models.CharField(max_length=25)
    ffss  = models.CharField(max_length=150)
    destinos = models.TextField(blank=True, null=True)
    weapon_assigned = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], blank=True, null=True) 
    weapon_number = models.CharField(max_length=50, blank=True, null=True) 
    studies = models.TextField(blank=True, null=True)
    certificaciones = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    efectivizacion_date = models.DateField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    privi_AD = models.CharField(max_length=50, blank=True, null=True)
    grupo_AD = models.CharField(max_length=50, blank=True, null=True)
    unidad = models.CharField(max_length=50, blank=True, null=True)
    ticket = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        db_table = 'miembros'
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'

    def __str__(self): 
        return self.name
    
    