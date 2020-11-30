from django.contrib import admin
from .models import Producto, Marca, Contacto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion', 'nuevo', 'marca', 'fecha_de_fabricacion']
    list_editable = ['nuevo']  # columna editable
    search_fields = ['nombre'] # busqueda por columna   
    list_filter = ['marca', 'nuevo', 'fecha_de_fabricacion'] # filtro por marca y nuevo
    # list_per_page = 2 # paginación(número de articulos por página)

admin.site.register(Producto, ProductoAdmin)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo', 'telefono', 'tipo_de_consulta', 'mensaje', 'avisos']
    list_editable = ['tipo_de_consulta']
    search_fields = ['nombre']
    list_filter = ['nombre', 'tipo_de_consulta']

admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Marca)