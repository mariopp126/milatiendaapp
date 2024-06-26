from .settings import *
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = False

# Configuración de la base de datos para el entorno de producción
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'milatiendard-db-1'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
