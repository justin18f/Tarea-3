from django.contrib import admin
from .models import Autor,Libro
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class LibroResource(resources.ModelResource):
    class Meta:
        model = Libro

class LibroAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo','fecha_publicacion',)
    resource_class = LibroResource

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor
        
class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre','apellidos']
    list_display = ('nombre','apellidos','estado',)
    resource_class = AutorResource

    
admin.site.register(Autor,AutorAdmin)
admin.site.register(Libro,LibroAdmin)
