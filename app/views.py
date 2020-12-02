from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca, Producto
from .forms import ContactoForm, ProductoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

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
        formulario = ContactoForm(data=request.POST) # formulario con datos
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Contacto guardado'
        else:
            data['form'] = formulario

    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')

def agregar_producto(request):   
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST or None, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Agregado correctamente.')
            return redirect('app:lista_de_productos')
        else:
            data['form'] = formulario
    
    return render(request, 'app/producto/agregar.html', data)

def lista_de_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 2) # mostramos 4 productos por página
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'page_obj': productos,     
        'paginator': paginator   
    }

    return render(request, 'app/producto/listar.html', data)


def modificar_producto(request, id):    
    # primero buscamos el producto
    producto = get_object_or_404(Producto, pk=id)
    data = {
        'form': ProductoForm(instance=producto) # llenamos el form con el producto buscado
    }

    if request.method == 'POST':
        # guardamos los datos del form
        formulario = ProductoForm(data=request.POST or None, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save() 
            messages.success(request, "Modificado correctamente.")
            return redirect('app:lista_de_productos')
        else:
            data['form'] = formulario

    return render(request, 'app/producto/modificar.html', data)

def eliminar_producto(request, id):
    # primero buscamos el producto
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente.")
    return redirect('app:lista_de_productos')
    
