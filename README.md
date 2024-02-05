# Procesador Flask DOCX a HTML

## Descripción
Esta aplicación Flask permite a los usuarios subir tablas en archivos DOCX para convertirlo a HTML accesible.

## Instalación

### Prerrequisitos
- Python 3.6 o superior
- Node.js y NPM
- pip y/o Conda para instalar dependencias de Python

### Configuración del Entorno

#### Dependencias de Python
##### Usando pip

```bash
pip install Flask BeautifulSoup4 pypandoc
```

##### Usando Conda

1. Crea un nuevo entorno Conda (reemplaza `myenv` con el nombre de tu entorno):

```bash
conda create -n myenv python=3.6
```

2. Activa el entorno:

```bash
conda activate myenv
```

3. Instala los paquetes necesarios:

```bash
conda install Flask
conda install -c anaconda beautifulsoup4
conda install -c conda-forge pypandoc
```

#### Dependencias de Node.js
Instala las dependencias de Node.js (TailwindCSS) utilizando NPM:

1. Navega al directorio del proyecto.
2. Ejecuta el siguiente comando:

```bash
npm install
```

### Ejecutando la Aplicación
En el directorio del proyecto ejecuta:

```bash
python app.py
```

La aplicación se iniciará en `localhost` con el puerto predeterminado `5000`. Accede a ella navegando a `http://localhost:5000` en el navegador.

## Licencia
Este proyecto está licenciado bajo la [Licencia MIT](https://opensource.org/licenses/MIT).