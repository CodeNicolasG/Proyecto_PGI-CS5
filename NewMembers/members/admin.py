from django.contrib import admin
from .models import Miembro

class MiembroAdmin(admin.ModelAdmin):
    list_display = ('name', 'dni', 'legajo', 'address', 'email_institucional', 'email_personal', 'phone_personal', 'phone_emergency', 'ffss', 'destinos', 'weapon_assigned', 'weapon_number', 'studies', 'certificaciones', 'skills', 'start_date', 'efectivizacion_date', 'experience', 'privi_AD', 'grupo_AD', 'unidad', 'ticket')
    search_fields = ['name', 'dni', 'legajo', 'address', 'email_institucional', 'email_personal', 'phone_personal', 'phone_emergency', 'ffss', 'destinos', 'weapon_assigned', 'weapon_number', 'studies', 'certificaciones', 'skills', 'start_date', 'efectivizacion_date', 'experience', 'privi_AD', 'grupo_AD', 'unidad', 'ticket']

admin.site.register(Miembro, MiembroAdmin)
