from django.shortcuts import render
from .models import Marca, Producto
from .forms import ContactoForm

# Create your views here.
def home(request):
    lista_de_productos = Producto.objects.all()
    context = {'lista_de_productos': lista_de_productos}
    return render(request, 'app/home.html', context)

def contacto(request):
    # creamos una instancia con el formulario vacio
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST) # formularrio con datos
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Contacto guardado'
        else:
            data['form'] = formulario

    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')