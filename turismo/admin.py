from django.contrib import admin
from .models import LugarTuristico

@admin.register(LugarTuristico)
class LugarTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'categoria', 'fecha_creacion')
    search_fields = ('nombre', 'ciudad', 'categoria')
    list_filter = ('ciudad', 'categoria')