from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User

class ObraArte(models.Model):
    ESTILOS = [
        ('impresionismo', 'Impresionismo'),
        ('romanticismo', 'Romanticismo'),
        ('surrealismo', 'Surrealismo'),
        # Agrega más estilos según sea necesario
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='obras/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estilo = models.CharField(max_length=50, choices=ESTILOS)
    artista = models.ForeignKey(User, on_delete=models.CASCADE, related_name='obras_como_artista_api')
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='obras_como_creador_api')

    class Meta:
        permissions = [
            ("can_edit_all_obras", "Can edit all obras"),
            ("can_delete_all_obras", "Can delete all obras"),
        ]

def __str__(self):
        return self.titulo