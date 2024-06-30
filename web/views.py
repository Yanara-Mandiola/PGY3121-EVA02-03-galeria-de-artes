from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .forms import ObraArteForm
from .forms import UserUpdateForm
from django.contrib import messages
from .models import Contacto
from .forms import UserPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from api.models import ObraArte
from .models import Evento
from django.utils import timezone
from .models import Evento
from .forms import PerfilForm
from django.contrib.auth import authenticate, login
from .models import Perfil

def index(request):
    obras = ObraArte.objects.all().order_by('-fecha_creacion')[:3]
    artistas_destacados = User.objects.filter(obras_como_artista_api__isnull=False).distinct()[:3]
    eventos = Evento.objects.filter(fecha__gte=timezone.now()).order_by('fecha')[:3]
    
    context = {
        'obras': obras,
        'artistas_destacados': artistas_destacados,
        'eventos': eventos,
    }
    return render(request, 'index.html', context)



def galeria(request):
    obras = ObraArte.objects.all()
    return render(request, 'galeria.html', {'obras': obras})


def impresionismo(request):
    obras = ObraArte.objects.filter(estilo='impresionismo')
    return render(request, 'impresionismo.html', {'obras': obras})

def romanticismo(request):
    obras = ObraArte.objects.filter(estilo='romanticismo')
    return render(request, 'romanticismo.html', {'obras': obras})

def surrealismo(request):
    obras = ObraArte.objects.filter(estilo='surrealismo')
    return render(request, 'surrealismo.html', {'obras': obras})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        Contacto.objects.create(nombre=nombre, email=email, mensaje=mensaje)
        return redirect('contacto')  # Redirigir después de enviar el formulario
    return render(request, 'contacto.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Asegúrate de que el usuario tenga un perfil
            Perfil.objects.get_or_create(usuario=user)
            return redirect('index')  # o cualquier otra página después del login
        else:
            # Mensaje de error
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')



@login_required
def publicar_obra(request):
    if request.method == 'POST':
        form = ObraArteForm(request.POST, request.FILES)
        if form.is_valid():
            obra = form.save(commit=False)
            obra.artista = request.user
            obra.creador = request.user
            obra.save()
            return redirect('galeria')
    else:
        form = ObraArteForm()
    return render(request, 'publica-ahora.html', {'form': form})



# @login_required
# def publicar_obra(request):
#     if request.method == 'POST':
#         form = ObraArteForm(request.POST, request.FILES)
#         if form.is_valid():
#             obra = form.save(commit=False)
#             obra.creador = request.user  # Asigna el usuario actual como creador
#             obra.save()
#             return redirect('detalle_obra', obra_id=obra.id)
#     else:
#         form = ObraArteForm()
#     return render(request, 'publicar_obra.html', {'form': form})









def logout_view(request):
    logout(request)
    return redirect('index')



def registrar_usuario(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = PerfilForm(request.POST, request.FILES)
        print("User form is valid:", user_form.is_valid())
        print("Profile form is valid:", profile_form.is_valid())
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.usuario = user
            profile.save()
            login(request, user)
            return redirect('index')
        else:
            print("User form errors:", user_form.errors)
            print("Profile form errors:", profile_form.errors)
    else:
        user_form = UserCreationForm()
        profile_form = PerfilForm()
    return render(request, 'registrar-usuario.html', {'user_form': user_form, 'profile_form': profile_form})




@login_required
def mi_cuenta(request):
    return render(request, 'mi-cuenta.html', {'user': request.user})



@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado.')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'editar-perfil.html', {'form': form})




@login_required
def dashboard_contacto(request):
    contactos = Contacto.objects.all()
    form_contrasena = UserPasswordChangeForm(request.user)
    return render(request, 'dashboard-contacto.html', {'contactos': contactos, 'form_contrasena': form_contrasena})




@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña ha sido actualizada.')
    else:
        form = UserPasswordChangeForm(request.user)
    return render(request, 'dashboard-contacto.html', {'form_contrasena': form})



@login_required
def cambiar_estado_contacto(request, contacto_id, nuevo_estado):
    try:
        contacto = Contacto.objects.get(id=contacto_id)
        contacto.estado = nuevo_estado
        contacto.save()
    except Contacto.DoesNotExist:
        pass  # Manejar el caso cuando el contacto no existe

    return redirect('dashboard_contacto')




@permission_required('api.can_edit_all_obras', raise_exception=True)
def editar_obra(request, obra_id):
    obra = get_object_or_404(ObraArte, id=obra_id)
    # Aquí iría la lógica para editar la obra
    # Por ejemplo:
    if request.method == 'POST':
        form = ObraArteForm(request.POST, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('detalle_obra', obra_id=obra.id)
    else:
        form = ObraArteForm(instance=obra)
    return render(request, 'editar_obra.html', {'form': form})

@permission_required('api.can_delete_all_obras', raise_exception=True)
def eliminar_obra(request, obra_id):
    obra = get_object_or_404(ObraArte, id=obra_id)
    # Aquí iría la lógica para eliminar la obra
    # Por ejemplo:
    if request.method == 'POST':
        obra.delete()
        return redirect('lista_obras')
    return render(request, 'confirmar_eliminar_obra.html', {'obra': obra})


def lista_obras(request):
    obras = ObraArte.objects.all()
    return render(request, 'lista_obras.html', {'obras': obras})

def detalle_obra(request, obra_id):
    obra = get_object_or_404(ObraArte, id=obra_id)
    return render(request, 'detalle_obra.html', {'obra': obra})

@login_required
def crear_obra(request):
    if request.method == 'POST':
        form = ObraArteForm(request.POST, request.FILES)
        if form.is_valid():
            obra = form.save(commit=False)
            obra.creador = request.user
            obra.save()
            return redirect('detalle_obra', obra_id=obra.id)
    else:
        form = ObraArteForm()
    return render(request, 'crear_obra.html', {'form': form})

@login_required
def editar_obra(request, obra_id):
    obra = get_object_or_404(ObraArte, id=obra_id)
    if request.user != obra.creador and not request.user.has_perm('api.can_edit_all_obras'):
        return redirect('detalle_obra', obra_id=obra.id)
    
    if request.method == 'POST':
        form = ObraArteForm(request.POST, request.FILES, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('detalle_obra', obra_id=obra.id)
    else:
        form = ObraArteForm(instance=obra)
    return render(request, 'editar_obra.html', {'form': form, 'obra': obra})

@login_required
def eliminar_obra(request, obra_id):
    obra = get_object_or_404(ObraArte, id=obra_id)
    if request.user != obra.creador and not request.user.has_perm('api.can_delete_all_obras'):
        return redirect('detalle_obra', obra_id=obra.id)
    
    if request.method == 'POST':
        obra.delete()
        return redirect('lista_obras')
    return render(request, 'confirmar_eliminar_obra.html', {'obra': obra})




def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def lista_obras(request):
    obras = ObraArte.objects.all()
    return render(request, 'lista_obras.html', {'obras': obras})

@login_required
@user_passes_test(is_superuser)
def detalle_obra(request, obra_id):
    obra = get_object_or_404(ObraArte, id=obra_id)
    return render(request, 'detalle_obra.html', {'obra': obra})

@login_required
@user_passes_test(is_superuser)
def crear_obra(request):
    if request.method == 'POST':
        form = ObraArteForm(request.POST, request.FILES)
        if form.is_valid():
            obra = form.save(commit=False)
            obra.creador = request.user
            obra.save()
            return redirect('detalle_obra', obra_id=obra.id)
    else:
        form = ObraArteForm()
    return render(request, 'crear_obra.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def editar_obra(request, obra_id):
    obra = get_object_or_404(ObraArte, id=obra_id)
    if request.method == 'POST':
        form = ObraArteForm(request.POST, request.FILES, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('detalle_obra', obra_id=obra.id)
    else:
        form = ObraArteForm(instance=obra)
    return render(request, 'editar_obra.html', {'form': form, 'obra': obra})

@login_required
@user_passes_test(is_superuser)
def eliminar_obra(request, obra_id):
    obra = get_object_or_404(ObraArte, id=obra_id)
    if request.method == 'POST':
        obra.delete()
        return redirect('lista_obras')
    return render(request, 'confirmar_eliminar_obra.html', {'obra': obra})