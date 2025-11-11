from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import LugarTuristico
from .forms import RegistroForm, LugarForm


# --- Utilidad para verificar si el usuario es admin del proyecto ---
def es_admin_proyecto(user):
    return user.is_staff  # o user.is_superuser según prefieras


# --- Autenticación ---
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Inicia sesión para continuar.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})


def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('lista_lugares')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'login.html')


@login_required
def logout_usuario(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return render(request, 'logout.html')


# --- Vistas principales ---
def lista_lugares(request):
    lugares = LugarTuristico.objects.all()
    return render(request, 'turismo/lista_lugares.html', {'lugares': lugares})


def detalle_lugar(request, pk):
    lugar = get_object_or_404(LugarTuristico, pk=pk)
    # Solo usuarios autenticados pueden ver detalles completos
    if not request.user.is_authenticated:
        raise PermissionDenied
    return render(request, 'turismo/detalle_lugar.html', {'lugar': lugar})


# --- CRUD restringido al admin del proyecto ---
@login_required
def crear_lugar(request):
    if not request.user.is_staff:
        raise PermissionDenied
    if request.method == 'POST':
        form = LugarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lugar creado correctamente.')
            return redirect('lista_lugares')
    else:
        form = LugarForm()
    return render(request, 'turismo/crear_lugar.html', {'form': form})


@login_required
def editar_lugar(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    lugar = get_object_or_404(LugarTuristico, pk=pk)
    form = LugarForm(request.POST or None, request.FILES or None, instance=lugar)
    if form.is_valid():
        form.save()
        messages.success(request, 'Lugar actualizado.')
        return redirect('detalle_lugar', pk=lugar.pk)
    return render(request, 'turismo/editar_lugar.html', {'form': form, 'lugar': lugar})


@login_required
def eliminar_lugar(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    lugar = get_object_or_404(LugarTuristico, pk=pk)
    if request.method == 'POST':
        lugar.delete()
        messages.warning(request, 'Lugar eliminado correctamente.')
        return redirect('lista_lugares')
    return render(request, 'turismo/eliminar_lugar.html', {'lugar': lugar})


# --- Errores personalizados ---
def error_403(request, exception=None):
    return render(request, 'turismo/403.html', status=403)

def error_404(request, exception=None):
    return render(request, 'turismo/404.html', status=404)