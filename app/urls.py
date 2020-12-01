from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('galeria/', views.galeria, name='galeria'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('lista-productos/', views.lista_de_productos, name='lista_de_productos'),
    path('modificar-producto/<int:id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<int:id>/', views.eliminar_producto, name="eliminar_producto"),
]