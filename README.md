## instalar dependecias/paquetes python en un en un entorno virtual.

### abrir la terminal del sistema y ejecutar:
```bash
python3
```
si se ejecuta correctamente python3 esta instalado correctamente de lo contrario se debe instalar y configurar la varaible PATH con la direccion donde se haya instalado python3

##### link tutorial
https://datatofish.com/add-python-to-windows-path/

#### repetir el paso anterior hasta conseguir obtener la siguiente salida. usar python como alternativa a python3 si no funciona
```bash
python3

Python 3.7.4 (default, Sep  7 2019, 18:27:02) 
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

### clonar este repositorio en tu equipo.
para esto descargar/instalar git. https://git-scm.com/downloads
ejecutar en la terminal los siguientes comandos, estos haran lo siguiente
1.- ir al directorio raiz(disco c) o puedes usar el que gustes
2.- clonar el repositorio(descarga una carpeta con todos los archivos)
3.- moverse al repositorio clonado
```bash
cd C:
git clone git@github.com:ale180192/cooking_point.git
cd cooking_point
```

#### crear el entorno virtual de python
Este entorno virtual hace que todos los paquetes que instales cuando el entorno este activo se instalen en el. Es basicamente una carpeta donde se instalaran los paquetes de python
```bash
python3 -m venv myvenv
```

#### activar el entorno virtual
```bash
\env\Scripts\activate.bat
```

#### Instalar los paquetes python. Estos se instalaran en el entorno virtual. usar pip3 si no funciona
```bash
pip install -r requirements.txt
```

### Ejecutar proceso.
```bash
python3 main.py
```


### instalacion de nuevos paquetes
Actualizar el archivo que contiene listadas todas las dependencias del proyecto
```bash
pip freeze >> requirements.txt
```