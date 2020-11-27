from django.contrib import admin
from .models import Producto, Marca

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion', 'nuevo', 'marca', 'fecha_de_fabricacion']
    list_editable = ['nuevo']  # columna editable
    search_fields = ['nombre'] # busqueda por columna   
    list_filter = ['marca', 'nuevo', 'fecha_de_fabricacion'] # filtro por marca y nuevo
    list_per_page = 2 # paginación(número de articulos por página)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Marca)