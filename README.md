# CustomLab API

CustomLab API es la API REST de nuestra tienda online, encargada de gestionar toda la lógica de negocio del sistema.

Está desarrollada con Python, Django y Django REST Framework, siguiendo una arquitectura por capas que separa responsabilidades y facilita el mantenimiento y la escalabilidad.

---

## Tecnologías

- Python 3.12
- Django – Framework web
- Django REST Framework – Creación de APIs REST
- PostgreSQL – Base de datos relacional
- Docker – Contenerización del entorno

---

## Estructura del Proyecto

El proyecto sigue una arquitectura de 3 capas (Controllers, Services y Repositories):

customlab_api/          # Configuración principal de Django

customlab_controllers/  # Controladores (vistas de la API)
└── controllers/
    ├── productoController.py
    └── usuarioController.py

customlab_services/     # Lógica de negocio
└── services/
    ├── productoService.py
    └── usuarioService.py

customlab_models/       # Acceso a datos (repositorios)
└── repositories/
    ├── productoRepository.py
    └── usuarioRepository.py

---

## Instalación

1. Clonar el repositorio

git clone <repositorio>
cd CustomLab_API

2. Crear y activar el entorno virtual

Windows:
python -m venv venv
.\venv\Scripts\Activate.ps1

Linux:
python3 -m venv venv
source venv/bin/activate

3. Instalar dependencias

pip install -r requirements.txt

4. Ejecutar migraciones

python manage.py migrate

---

## Ejecución

Desarrollo local:
python manage.py runserver

Con Docker:
docker compose up

---

## Arquitectura

El proyecto sigue un patrón de 3 capas:

- Controllers: reciben las peticiones HTTP y devuelven las respuestas
- Services: contienen la lógica de negocio
- Repositories: acceden directamente a la base de datos

---

## Endpoints Principales

Productos:
- GET /api/productos/
- GET /api/productos/{id}/
- POST /api/productos/
- PUT /api/productos/{id}/
- DELETE /api/productos/{id}/

Usuarios:
- GET /api/usuarios/
- GET /api/usuarios/{id}/
- POST /api/usuarios/
- PUT /api/usuarios/{id}/
- DELETE /api/usuarios/{id}/

---

## Autores

David Juncosa & Moussa Boudhafri
