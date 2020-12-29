from django.urls import path, include
from . import views
from rest_framework import routers, viewsets

# definimos las rutas
router = routers.DefaultRouter() # ruta base
router.register('producto', views.ProductoViewset)
router.register('marca', views.MarcaViewset)

# ejemplo: localhost:8000/api/producto

app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('galeria/', views.galeria, name='galeria'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('lista-productos/', views.lista_de_productos, name='lista_de_productos'),
    path('modificar-producto/<int:id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<int:id>/', views.eliminar_producto, name="eliminar_producto"),
    path('registro/', views.registro, name='registro'),
    path('error-facebook/', views.error_facebook, name="error_facebook"),
    path('api/', include(router.urls)),
]