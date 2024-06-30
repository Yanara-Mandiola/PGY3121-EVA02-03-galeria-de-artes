from django import forms
from api.models import ObraArte
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from api.models import ObraArte
from .models import Perfil


from api.models import ObraArte



class ObraArteForm(forms.ModelForm):
    class Meta:
        model = ObraArte
        fields = ['titulo', 'descripcion', 'imagen', 'estilo']
        widgets = {
            'estilo': forms.Select(choices=ObraArte.ESTILOS)
        }




class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']




class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})


        


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'bio']  # Reemplaza con los campos reales de tu modelo Perfil
