from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('realizado', 'Realizado'),
    ], default='pendiente')

    def __str__(self):
        return f"{self.nombre} - {self.email}"
    

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()

    def __str__(self):
        return self.titulo
    



class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    avatar = models.ImageField(upload_to='avatares/', default='avatares/default.png')
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

@receiver(post_save, sender=User)
def crear_o_actualizar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
    else:
        instance.perfil.save()



    
    

# class ObraArte(models.Model):
#     titulo = models.CharField(max_length=200)
#     descripcion = models.TextField()
#     imagen = models.ImageField(upload_to='obras/')
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     estilo = models.CharField(max_length=50)
#     artista = models.ForeignKey(User, on_delete=models.CASCADE, related_name='obras_como_artista')
#     creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='obras_como_creador')

#     class Meta:
#         permissions = [
#             ("can_edit_all_obras", "Can edit all obras"),
#             ("can_delete_all_obras", "Can delete all obras"),
#         ]

#     def __str__(self):
#         return self.titulo