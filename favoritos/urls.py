from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_favoritos, name='lista_favoritos'),
    path('agregar/<int:lugar_id>/', views.agregar_favorito, name='agregar_favorito'),
    path('quitar/<int:lugar_id>/', views.quitar_favorito, name='quitar_favorito'),
]
