
from .models import Producto, Marca
from rest_framework import serializers
from .validators import MaxSizeFileValidator
from django.core.exceptions import ValidationError

# Serializers define la representación de la API
class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):

    nombre_marca = serializers.CharField(read_only=True, source="marca.nombre")
    marca = MarcaSerializer(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source="marca")

    # validaciones
    nombre = serializers.CharField(required=True, min_length=3)
    precio = serializers.DecimalField(max_digits=10, decimal_places=3, min_value=1)
    image = serializers.FileField(required=False, validators=[MaxSizeFileValidator(max_file_size=1)])

    # valida los nombres de productos repetidos
    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre =value).exists() # validamos si existe en nombre en la DB

        if existe:
            raise serializers.ValidationError("Este nombre de producto ya existe")

        return value

    class Meta:
        model = Producto
        fields = '__all__'