import streamlit as st

# Título principal
st.title("Imágenes y Contenedores Docker")

# Sección: Imágenes Docker
st.header("Imágenes Docker")

# Definición de imágenes Docker
st.subheader("Definición")
st.write("""
- Son plantillas inmutables que contienen todo lo necesario para ejecutar una aplicación.
- Son la base de los contenedores Docker, y permiten la portabilidad de aplicaciones entre diferentes entornos.
""")

# Contenido de una imagen
st.subheader("Contenido de una Imagen")
st.write("""
Una imagen incluye el código de la aplicación, bibliotecas, dependencias, herramientas, configuraciones del sistema, 
y cualquier otra cosa que la aplicación necesite para funcionar correctamente.
""")

# Dockerfile
st.subheader("Dockerfile")
st.write("""
Es un archivo de texto que contiene una serie de instrucciones para construir una imagen. Algunas de las instrucciones más comunes son:
""")

# Ejemplo de instrucciones Dockerfile
st.code("""
FROM: establece una imagen base.
RUN: ejecuta comandos dentro de la imagen.
COPY: copia archivos locales dentro de la imagen.
""", language="docker")

# Construcción de imágenes
st.subheader("Construcción de Imágenes")
st.write("""
Las imágenes se crean utilizando el comando `docker build`, que toma un Dockerfile y lo convierte en una imagen. 
Cada paso en el Dockerfile genera una nueva capa de la imagen, permitiendo reutilizar partes de la misma para mejorar la eficiencia.
""")

# Repositorios y distribución
st.subheader("Repositorios y Distribución")
st.write("""
Las imágenes se almacenan en registros como Docker Hub, donde pueden ser descargadas y compartidas. 
Una imagen se identifica por su nombre y versión (o tag). Por ejemplo, `nginx:latest` hace referencia a la versión más reciente de la imagen de Nginx.
""")

# Sección: Contenedores Docker
st.header("Contenedores Docker")

# Definición de contenedores Docker
st.subheader("Definición")
st.write("""
- Son instancias en ejecución de imágenes Docker.
- Proporcionan un entorno aislado para que las aplicaciones se ejecuten de forma independiente y sin interferir con el sistema host o con otros contenedores.
""")

# Aislamiento de contenedores
st.subheader("Aislamiento de Contenedores")
st.write("""
Cada contenedor ejecuta su propia copia del sistema de archivos, red, y tiene su propio espacio de procesos, 
gracias a tecnologías como namespaces y cgroups de Linux. Esto permite que múltiples contenedores se ejecuten en un mismo host sin conflictos.
""")

# Livianos y eficientes
st.subheader("Livianos y Eficientes")
st.write("""
A diferencia de las máquinas virtuales, los contenedores comparten el kernel del sistema operativo, lo que los hace mucho más ligeros 
en términos de consumo de recursos y tiempo de arranque. Por ejemplo, mientras una máquina virtual puede consumir gigabytes de RAM, 
un contenedor suele consumir solo unos pocos megabytes.
""")

# Persistencia de datos
st.subheader("Persistencia de Datos")
st.write("""
Aunque los contenedores son efímeros (sus datos desaparecen al detenerse), los datos pueden mantenerse persistentes mediante el uso de **volúmenes**.
Los volúmenes permiten almacenar datos fuera del ciclo de vida del contenedor y compartirlos entre múltiples contenedores.
""")

# Administración de contenedores
st.subheader("Administración")
st.write("""
Los contenedores pueden ser iniciados, detenidos, replicados y eliminados fácilmente con los siguientes comandos:
""")
st.code("""
docker run: para iniciar un contenedor.
docker stop: para detener un contenedor.
docker rm: para eliminar un contenedor.
""", language="bash")

# Diferencias clave entre Imágenes y Contenedores
st.header("Diferencias clave entre Imágenes y Contenedores")

st.subheader("Imágenes")
st.write("""
- Son archivos estáticos que definen el entorno de una aplicación.
- No cambian durante su uso, se crean una vez y se reutilizan.
- Son plantillas que especifican cómo debe ser el contenedor.
""")

st.subheader("Contenedores")
st.write("""
- Son instancias dinámicas de imágenes que se ejecutan en el sistema.
- Tienen un ciclo de vida: pueden iniciarse, ejecutarse, detenerse y eliminarse.
- Son el entorno real donde la aplicación está funcionando.
""")
