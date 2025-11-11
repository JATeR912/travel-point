from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from turismo import views as turismo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('turismo.urls')),
]

# Handlers de errores personalizados
handler403 = turismo_views.error_403
handler404 = turismo_views.error_404

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)