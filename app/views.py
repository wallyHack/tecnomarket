from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca, Producto
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required
def home(request):
    lista_de_productos = Producto.objects.all()
    context = {'lista_de_productos': lista_de_productos}
    return render(request, 'app/home.html', context)

@login_required
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

@login_required
def galeria(request):
    return render(request, 'app/galeria.html')

@permission_required('app.add_producto')
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

@permission_required('app.view_producto')
def lista_de_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 3) 
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'page_obj': productos,     
        'paginator': paginator   
    }

    return render(request, 'app/producto/listar.html', data)


@permission_required('app.change_producto')
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

@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    # primero buscamos el producto
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente.")
    return redirect('app:lista_de_productos')
    
def registro(request):
    # contexto que se renderiza al template
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            # una vez creado el usuario, lo autenticamos y logeamos
            user = authenticate(username=formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            # redireccionamos al home
            return redirect("app:home")

        data['form'] = formulario

    return render(request, 'registration/registro.html', data)
