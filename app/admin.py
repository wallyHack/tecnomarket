from django.contrib import admin
from .models import Producto, Marca

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'precio', 'descripcion', 'nuevo', 'marca', 'fecha_de_fabricacion']
    list_filter = ['fecha_de_fabricacion']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Marca)