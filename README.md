# Aplicación de control del turno

Pensado para épocas de matrícula, donde existe una gran afluencia de personas, esta aplicación permite mostrar en una pantalla el número del turno y además controlarlo desde otro(s) equipo(s).

## Configuración

1. Crear 3 ficheros de configuración:

`./config.js`:

~~~javascript
var wsPort = "9001";  // especificar el valor correspondiente
~~~

`./screen/config.js`:

~~~javascript
var wsHost = "localhost";  // especificar el valor correspondiente
~~~

`./admin/config.js`:

~~~javascript
var wsHost = "localhost";  // especificar el valor correspondiente
~~~

2. Lanzar el servidor de *websockets*:

~~~console
$ run_ws-server.sh
~~~

> Referencia: https://github.com/Pithikos/python-websocket-server

3. Abrir en un navegador la visualización del número de turno: `/turno/screen/`

4. Abrir en otro equipo la interfaz de control: `/turno/admin`
