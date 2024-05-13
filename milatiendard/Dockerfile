# Usa una base de imagen con Python
FROM python:3.12

# Establece el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias del proyecto
RUN pip install -r requirements.txt

# Copiar archivo de configuración específico (por ejemplo, settings.prod.py)
#COPY milatiendard/settings_prod.py /app/settings.py

# Expone el puerto en el que Django correrá
EXPOSE 8000

# El comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
