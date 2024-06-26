import os
from .settings import *
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

# Configuración de la base de datos para el entorno local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'db_milatienda'),
        'USER': os.environ.get('DB_USER', 'admin_mila'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'milaadmin1234'),
        'HOST': os.environ.get('localhost'),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}
