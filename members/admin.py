from django.contrib import admin
from django.http import HttpResponse
from import_export.admin import ExportMixin
from import_export.resources import ModelResource
from import_export.formats.base_formats import XLSX, JSON, CSV  # Elimina PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Miembro

# Definir un recurso para el modelo Miembro
class MiembroResource(ModelResource):
    class Meta:
        model = Miembro

@admin.register(Miembro)
class MiembroAdmin(ExportMixin, admin.ModelAdmin):  # ExportMixin habilita los formatos de exportación
    resource_class = MiembroResource
    formats = [XLSX, JSON, CSV]  # Formatos disponibles en el Admin

    list_display = ('name', 'dni', 'legajo', 'address', 'birth_date', 'ciudadania', 'provincia_de_nacimiento', 'ciudad_de_nacimiento', 
                    'email_institucional', 'email_personal', 
                    'phone_personal', 'phone_emergency', 'ffss', 'destinos', 'weapon_assigned', 
                    'weapon_number', 'studies', 'certificaciones', 'skills', 'start_date', 
                    'efectivizacion_date', 'experience', 'privi_AD', 'grupo_AD', 'unidad', 'ticket')

    search_fields = ['name', 'dni', 'legajo', 'address', 'birth_date', 'ciudadania', 'provincia_de_nacimiento', 'ciudad_de_nacimiento',
                     'email_institucional', 'email_personal', 
                     'phone_personal', 'phone_emergency', 'ffss', 'destinos', 'weapon_assigned', 
                     'weapon_number', 'studies', 'certificaciones', 'skills', 'start_date', 
                     'efectivizacion_date', 'experience', 'privi_AD', 'grupo_AD', 'unidad', 'ticket']

    actions = ["exportar_pdf"]

    # Función personalizada para exportar a PDF
    def exportar_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="miembros.pdf"'

        # Crear documento PDF
        pdf = canvas.Canvas(response, pagesize=letter)
        pdf.setTitle("Lista de Miembros")

        # Encabezado
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(200, 750, "Lista de Miembros")

        pdf.setFont("Helvetica", 10)
        y = 720  # Posición inicial en el PDF

        # Agregar datos al PDF
        for miembro in queryset:
            pdf.drawString(50, y, f"Nombre: {miembro.name}")
            y -= 20  # Espaciado entre filas
            
            pdf.drawString(50, y, f"FFSS: {miembro.ffss}")
            y -= 20  # Espaciado entre filas
            
            pdf.drawString(50, y, f"Telefono: {miembro.phone_personal}")
            y -= 20  # Espaciado entre filas

            pdf.drawString(50, y, f"email institucional: {miembro.email_institucional}")
            y -= 20  # Espaciado entre filas

            pdf.drawString(50, y, f"DNI: {miembro.dni}")
            y -= 40  # Espaciado entre filas

            if y < 50:  # Salto de página si se llena la hoja
                pdf.showPage()
                pdf.setFont("Helvetica", 10)
                y = 750

        pdf.save()
        return response

    exportar_pdf.short_description = "Exportar seleccionados a PDF"  # Nombre en Django Admin
