# pymarktime

_Programa portable de consola para marcar entradas y salidas de empleados._

<img src="https://i.ibb.co/7NH4Zc0/pythonmarktime.png" alt="pythonmarktime" border="0" width="100">

## Requisitos:
- Tener el esquema de base de datos y seguir los pasos de su **README.md**. Esto lo encuentras en el repositorio _[pymarktime-DDBB](https://github.com/mrbean95/pymarktime-DDBB)_
- Python 3.12.4.

## Pasos:

#### 1.- Instalar las dependencias del proyecto: ####
```sh
pip install -r requirements.txt
```

#### 2.- Crear un archivo de texto plano con el nombre _.env_ ####

#### 3.- Dentro de _.env_ ingresar los siguientes datos: ####

```sh
DB_HOST='ip'
DB_USER='usuario'
DB_PASSWORD='contraseña'
```

Donde:

- **ip** es la dirección IP del equipo que contiene la base de datos.
- **usuario** es el usuario que tiene permisos para la base de datos.
- **contraseña** es la contraseña del usuario que tiene permisos para la base de datos.

Recuerda que los dos ultimos datos anteriores dependen de si creaste un usuario para la base de datos o usaras el usuario root.

#### 4.- Guarda el archivo. ####

#### 5.- Ejecuta el proyecto: ####

```sh
python main.py
```

#### 6.- Inicia sesión con el superusuario del sistema: ####

```sh
dni: 00000000
pass: 1234
```

## Caracteristicas del programa.

La función principal del programa es ser un programa de linea de comandos para marcar las horas de entrada y/o salida de empleados.

Las caracteristicas principales son:

- Realizar marcaciones (dia,mes,año, hora, fecha y segundo).
- Tiempo de espera antes de realizar otra marcación. Esta programado para 30 minutos por defecto.
- Registrar a un empleado desde el mismo programa.
- Inhabilitar a un empleado desde el mismo programa
- Habilitar a un empleado desde el mismo programa.
- Cambiar la contraseña desde el mismo programa
- Posibilidad de tener uno o más permisos.
