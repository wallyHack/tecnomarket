
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    # agregando estilos a elementos por separado
    # nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Contacto
        # fields = ['nombre', 'correo', 'telefono', 'tipo_de_consulta', 'mensaje', 'avisos']
        fields = '__all__'

        