from django.contrib import admin
from .models import ObraArte

# Register your models here.

class AdminObraArte(admin.ModelAdmin):
    list_display = ['titulo', 'creador', 'fecha_creacion']
    list_filter = ['creador', 'estilo']
    search_fields = ['titulo', 'descripcion']

    def has_change_permission(self, request, obj=None):
        if obj is None or request.user.is_superuser:
            return True
        return obj.creador == request.user

    def has_delete_permission(self, request, obj=None):
        if obj is None or request.user.is_superuser:
            return True
        return obj.creador == request.user

admin.site.register(ObraArte, AdminObraArte)
