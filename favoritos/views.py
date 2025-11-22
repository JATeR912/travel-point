from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from turismo.models import LugarTuristico
from .models import Favorito

@login_required
def agregar_favorito(request, lugar_id):
    lugar = get_object_or_404(LugarTuristico, id=lugar_id)
    favorito, creado = Favorito.objects.get_or_create(usuario=request.user, lugar=lugar)
    if creado:
        messages.success(request, f"{lugar.nombre} se agregó a tus favoritos.")
    else:
        messages.info(request, f"{lugar.nombre} ya estaba en tus favoritos.")
    return redirect('detalle_lugar', pk=lugar.id)

@login_required
def quitar_favorito(request, lugar_id):
    lugar = get_object_or_404(LugarTuristico, id=lugar_id)
    favorito = Favorito.objects.filter(usuario=request.user, lugar=lugar)
    if favorito.exists():
        favorito.delete()
        messages.warning(request, f"{lugar.nombre} se quitó de tus favoritos.")
    return redirect('detalle_lugar', pk=lugar.id)

@login_required
def lista_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user).select_related('lugar')
    return render(request, 'favoritos/lista_favoritos.html', {'favoritos': favoritos})
