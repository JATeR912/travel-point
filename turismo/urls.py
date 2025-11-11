from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_lugares, name='lista_lugares'),
    path('lugar/<int:pk>/', views.detalle_lugar, name='detalle_lugar'),
    path('lugar/nuevo/', views.crear_lugar, name='crear_lugar'),
    path('lugar/<int:pk>/editar/', views.editar_lugar, name='editar_lugar'),
    path('lugar/<int:pk>/eliminar/', views.eliminar_lugar, name='eliminar_lugar'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]