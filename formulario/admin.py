from django.contrib import admin
from .models import Incidente

@admin.register(Incidente)
class IncidenteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'area', 'fecha', 'que_ocurrio')
    readonly_fields = ('codigo',)  # 🔒 no editable
