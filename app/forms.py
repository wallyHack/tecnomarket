
from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    # agregando estilos a elementos por separado
    # nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Contacto
        # fields = ['nombre', 'correo', 'telefono', 'tipo_de_consulta', 'mensaje', 'avisos']
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    image = forms.FileField(required=False)
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