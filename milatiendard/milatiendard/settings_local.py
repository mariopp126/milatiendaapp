import os
from .settings import *

DEBUG = True

# Configuración de la base de datos para el entorno local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'mydatabase'),
        'USER': os.environ.get('DB_USER', 'mydatabaseuser'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'mypassword'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}
