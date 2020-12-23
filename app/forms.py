
from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.core.exceptions import ValidationError

class ContactoForm(forms.ModelForm):

    # agregando estilos a elementos por separado
    # nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Contacto
        # fields = ['nombre', 'correo', 'telefono', 'tipo_de_consulta', 'mensaje', 'avisos']
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    
    image = forms.FileField(required=False, validators=[MaxSizeFileValidator(max_file_size=1)]) # validamos que el campo imagen no sea requerido
    nombre = forms.CharField(min_length=3, max_length=10) 
    precio = forms.DecimalField(min_value=1)   
   
    # validación personalizada para que no se repita el nombre
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")

        return nombre

    class Meta:
        model = Producto        
        fields = '__all__'

        widgets = {
            "fecha_de_fabricacion": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']