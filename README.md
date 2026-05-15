# CustomLab API

**CustomLab API** es el núcleo backend y la API REST para la plataforma de tienda online CustomLab. Este sistema gestiona toda la lógica de negocio, autenticación de usuarios, gestión de productos y procesamiento de datos.

Este documento proporciona las instrucciones necesarias para la instalación, configuración y puesta en marcha del sistema, diferenciando entre los entornos de desarrollo y producción.

---

## Tecnologías Utilizadas

- **Backend:** Python 3.12 + Django 6.0 + Django REST Framework
- **Base de Datos:** PostgreSQL
- **Servidor Web & Proxy:** Nginx + Gunicorn
- **Seguridad:** Certbot (SSL Let's Encrypt) + JWT para autenticación
- **Despliegue:** Docker & Docker Compose

---

## Estructura del Proyecto

El proyecto sigue una arquitectura modular dentro de Django:

- `customlab_api/`: Configuración principal del proyecto, settings y rutas base.
- `customlab_models/`: Definición de los modelos de datos (tablas de la BD).
- `customlab_controllers/`: Lógica de los endpoints y vistas de la API (Controllers).
- `customlab_services/`: Lógica de negocio y servicios auxiliares.
- `nginx/`: Configuración del servidor proxy inverso.
- `certbot/`: Scripts y certificados para SSL (HTTPS).
- `BBDD_backup/`: Directorio destinado a las copias de seguridad de la base de datos.

---

## Requisitos Previos

Para instalar y ejecutar este software, asegúrese de tener instalado en su sistema:

1. **Git** (para clonar el repositorio).
2. **Docker** y **Docker Compose**.

---

## Puesta en Marcha (Docker)

El proyecto está completamente contenerizado, lo que simplifica la gestión de dependencias y configuración.

### 1. Pasos Comunes (Clonación y Configuración)
Independientemente del modo, primero debe clonar el repositorio y configurar el entorno:

```bash
git clone <URL_DEL_REPOSITORIO>
cd CustomLab_API
docker network create customlab_network
```

Cree un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
# Configuración de Django
DEBUG=1                   # 1 para desarrollo, 0 para producción
SECRET_KEY=tu_secret_key  # Generar una clave segura
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost:8000

# Base de Datos (PostgreSQL)
DB_NAME=customlab_db
DB_USER=customlab_user
DB_PASSWORD=customlab_password
DB_HOST=db
DB_PORT=5432

# DuckDNS (Solo producción)
DUCKDNS_TOKEN=tu_token
DUCKDNS_DOMAIN=tu_dominio
```

### 2. Entorno de Desarrollo
Para trabajar en local, el proyecto utiliza el archivo `docker-compose.override.yml` automáticamente. Este modo:
- Ejecuta el servidor de desarrollo de Django (`runserver`).
- Deshabilita Nginx y Certbot para evitar problemas de certificados SSL en local.
- Expone la API directamente en el puerto `8000`.

Para iniciar en modo desarrollo:
```bash
docker compose up
```
La API estará disponible en `http://localhost:8000/`.

### 3. Entorno de Producción
Para desplegar el sistema completo en producción:
- Utiliza **Gunicorn** como servidor de aplicaciones.
- Levanta **Nginx** como proxy inverso (puertos 8080/8443).
- Activa **Certbot** para la gestión de certificados SSL.

Para iniciar en modo producción:
```bash
docker compose -f docker-compose.yml up -d
```

---

## 🗄️ Gestión de Base de Datos

### Realizar un Backup
Para exportar el contenido actual de la base de datos a un archivo SQL:

```bash
docker exec -t customlab_db_local pg_dump -U customlab_user customlab_db > BBDD_backup/backup_$(date +%Y%m%d).sql
```

### Restaurar un Backup
Para importar un archivo de respaldo en la base de datos:

```bash
cat BBDD_backup/backup.sql | docker exec -i customlab_db_local psql -U customlab_user -d customlab_db
```
*Nota: Asegúrese de que el contenedor de la base de datos esté en ejecución antes de restaurar.*

---

## 👥 Autores y Soporte

Para cualquier duda o soporte técnico relacionado con la instalación:
- **David Juncosa**
- **Moussa Boudhafri**
