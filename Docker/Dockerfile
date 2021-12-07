# Imagen base
FROM python:3

# Cambiar directorio
WORKDIR /usr/src/app

# Copiar dependencias al contenedor
COPY requirements.txt ./

# Descargar e instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar ficheros al contenedor
COPY . .
