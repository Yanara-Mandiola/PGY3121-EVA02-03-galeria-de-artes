# Generated by Django 5.0.6 on 2024-06-29 20:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
        
class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_evento'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='avatares/default.png', upload_to='avatares/')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
