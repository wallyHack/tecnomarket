from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_de_fabricacion = models.DateField()
    image = models.ImageField(upload_to="productos", null=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre 

class Contacto(models.Model):
    TIPO_DE_CONSULTA = ( 
        ("0", "Consulta"), 
        ("1", "Reclamo"), 
        ("2", "Sugerencia"), 
        ("3", "Felicitaciones"), 
    )
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.IntegerField()
    tipo_de_consulta = models.CharField(max_length=50, choices=TIPO_DE_CONSULTA, default='0')
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
