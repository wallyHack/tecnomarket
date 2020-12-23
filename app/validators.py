
from django.core.exceptions import ValidationError

# validamos el tamaño de subida para una imagen
class MaxSizeFileValidator:

    def __init__(self, max_file_size=5):
        self.max_file_size = max_file_size

    def __call__(self, value): # valor recibido de la caja del formulario
        size  = value.size
        max_size = self.max_file_size * 1048576 # 1 MB = 1048576 bytes

        if size > max_size:
            raise ValidationError(f"El tamaño maximo del archivo debe de ser de {self.max_file_size}MB")

        return value

    
