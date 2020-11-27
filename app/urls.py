from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('galeria/', views.galeria, name='galeria'),
]