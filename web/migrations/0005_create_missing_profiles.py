from django.db import migrations

def crear_perfiles_faltantes(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Perfil = apps.get_model('web', 'Perfil')
    for user in User.objects.all():
        Perfil.objects.get_or_create(usuario=user)

class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_perfil'),  # Asegúrate de que este sea el nombre correcto de tu migración anterior
    ]

    operations = [
        migrations.RunPython(crear_perfiles_faltantes),
    ]
