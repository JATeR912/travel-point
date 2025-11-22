# TravelPoint

TravelPoint es una aplicación web desarrollada en Django que permite a los usuarios explorar y gestionar información sobre festivales en Japón, ofreciendo contenido dinámico mediante templates, funcionalidades de autenticación, favoritos y administración de datos. La plataforma facilita la planificación y descubrimiento de eventos culturales, y está diseñada de forma escalable para poder ampliar su cobertura a otros países o tipos de destinos turísticos en el futuro. Está diseñada para usuarios generales y administradores del proyecto, con control de acceso y CRUD de lugares turísticos.

---

## Características Principales

- **Exploración de lugares turísticos**: Los usuarios pueden ver información básica de los lugares, incluyendo nombre, ciudad e imagen.
- **Detalles completos para usuarios autenticados**: Solo los usuarios registrados pueden acceder a la descripción completa de los lugares.
- **Lista de favoritos para usuarios autenticados**: Solo los usuarios registrados pueden crear una lista con sus lugares favoritos.
- **CRUD de lugares turísticos**:  
  - Solo administradores del proyecto pueden crear, editar o eliminar lugares.  
  - Se implementa control de permisos con decoradores de Django.
- **Sistema de autenticación**: Registro, login y logout de usuarios.
- **Mensajes y notificaciones**: Retroalimentación sobre acciones de usuario (éxito, error, advertencia).
- **Control de acceso**:  
  - Usuarios no autenticados solo ven información básica y no pueden acceder a detalles completos.  
  - Intentos de acceso no autorizado generan error 403.  
  - Páginas de error personalizadas 403 y 404.
- **Panel de administración de Django**: Gestión de usuarios, roles y lugares desde el admin.
- **Sistema de plantillas responsive**: Uso de Bootstrap para un diseño moderno y adaptable.

---

## Estructura de Carpetas

```bash
travelpoint/
├─ manage.py
├─ travelpoint/             <-- Proyecto
│  ├─ urls.py
│  └─ settings.py
├─ turismo/                 <-- Aplicacion lugares turisticos
│  ├─ templates/turismo/
│  ├─ static/turismo/
│  │  ├─ js/
│  │  ├─ img/
│  │  └─ css/
│  │     └─ style.css
│  ├─ views.py
│  ├─ urls.py
│  └─ models.py
├─ favoritos/               <-- Aplicacion favoritos (usuarios autenticados)
│  ├─ templates/favoritos/
│  ├─ views.py
│  ├─ urls.py
│  └─ models.py
├─ templates/               <-- Templates generales
│  ├─ base.html
│  ├─ login.html
│  ├─ register.html
│  └─ logout.html
├─ static/                  <-- Archivos estaticos generales
│  ├─ js/
│  ├─ img/
│  └─ css/
│     └─ style.css
└─ media/
```

## Uso
Acceder a la página principal para ver la lista de lugares turísticos.

Registrarse o iniciar sesión para acceder a detalles completos y añadir a favoritos.

Solo administradores pueden crear, editar o eliminar lugares desde la interfaz web.

Intentar acceder a rutas no permitidas muestra errores 403 o 404 según corresponda.