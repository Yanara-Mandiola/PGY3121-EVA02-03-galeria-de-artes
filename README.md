# Galeria-Arte

Galeria-Arte es una aplicación web desarrollada con Django que permite a los artistas publicar y compartir sus obras de arte digitales. Los usuarios pueden explorar la galería, filtrar por estilos artísticos y registrarse para publicar sus propias obras.

## Requisitos

- Python 3.x
- pip (administrador de paquetes de Python)
- MySQL o cualquier otro motor de base de datos compatible con Django

## Instalación

1. Clona este repositorio:


2. Navega al directorio del proyecto:

cd galeria-arte


3. Crea un entorno virtual y actívalo:

python -m venv env source env/bin/activate # En Windows, usa env\Scripts\activate


4. Instala las dependencias del proyecto:

pip install -r requirements.txt


5. Configura la base de datos en `galeria_arte/settings.py`.

6. Realiza las migraciones de la base de datos:

python manage.py migrate


7. Crea un superusuario para acceder al admin de Django:

python manage.py createsuperuser


## Ejecución

1. Inicia el servidor de desarrollo:

python manage.py runserver


2. Abre un navegador web y visita `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

## Uso

- Explora la galería de obras de arte en la página principal.
- Regístrate como usuario para publicar tus propias obras.
- Inicia sesión y ve a la página "Publicar" para cargar una nueva obra.
- Filtra las obras por estilo artístico utilizando los enlaces en la navegación.


## Comandos básicos para ejecutar la aplicación

### Configuración inicial

1. Clonar el repositorio:
python -m venv venv source venv/bin/activate # En Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations python manage.py migrate

python manage.py runserver

La aplicación estará disponible en `http://127.0.0.1:8000/`

### Comandos adicionales útiles

- Crear un superusuario:

python manage.py createsuperuser

python manage.py collectstatic


- Ejecutar tests:
python manage.py test

-restaurar bbdd:
python manage.py flush
