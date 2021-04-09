# Challenge MercadoLibre - Creación de una API para facilitar consultas sobre la API de Google Drive

## Autor ✒️

* **Leonardo Di Carlo** - [leonardodicarlo](https://github.com/leonardodicarlo)


## Instalación 🔧

_Para correr nuestra API es necesario instalar las siguientes dependencias (válido para bash):
```
$ sudo apt-get install build-essential libssl-dev libffi-dev python3-dev cargo
```
```
$ sudo pip3 install PyDrive2
```

## Gestión de credenciales 🔑

_En este repositorio ya se encuentra asignada la cuenta de Gmail challengemelidicarlo@gmail.com con su respectiva contraseña de manera ejemplificada. Para utilizar la API con una cuenta propia de Google deben seguirse los siguientes pasos:_


* Primeramente, borrar el archivo **client_secrets.json** presente en este repositorio. Se debe obtener el archivo client_secrets.json desde la cuenta de Gmail con la que se desea loguearse a través de la plataforma Google Cloud Platform (realizando la configuración necesaria del protocolo OAuth - ver [link](https://developers.google.com/workspace/guides/create-credentials)). Luego, también borrar el archivo **settings.yaml** ya que se generará uno nuevo con las credenciales ingresadas.

* Una vez obtenido el propio archivo client_secrets.json, debe agregarlo donde tenga clonado este repositorio. Luego, ejecute el script **pyDrive.py** en su IDE o compilador y verá que se le generará un link al que debe acceder e ingresar sus credenciales manualmente. Ingresando allí quedará logueado en tanto dure la ejecución del script **APIDrive.py** .

* En caso de que quiera mantener sus credenciales guardadas automáticamente, debe crear un nuevo archivo **settings.yaml**. Puede tomar como base el ya existente, sólo que debe ingresar en los campos 'client_id' y 'client_secret' los valores que usted tiene en su propio archivo client_secrets.json.

* Luego, debe volver a ejecutar el script **pyDrive.py**, ingresar nuevamente al link generado, y por último ingresar nuevamente sus credenciales manualmente. Si todo se realizó correctamente, verá que se crea un archivo llamado **credentials_module.json**.

* Por último, debe ejecutar el script **APIDrive.py** en su IDE o compilador y ¡listo!, la API está corriendo en su localhost:4000

## Ejecución - Comandos soportados 📋

_Siguiendo el contrato mencionado en el enunciado del Challenge, la API soporta los siguientes requests:

```
GET localhost:4000/ (esta es la ruta raíz y sólo devolverá un mensaje "Bienvenido a la API para búsquedas en Drive").
```
```
GET localhost:4000/search-in-doc/UNID?word=UNAPALABRA  (tenga en cuenta que UNID y UNAPALABRA se deben ingresar como parámetros para respetar el contrato).
```
```
POST localhost:4000/file?titulo=UNTITULO&descripcion=UNADESCRIPCION (nuevamente UNTITULO y UNADESCRIPCION se deben ingresar como parámetros para cumplir la consigna).
```

## Muchas gracias!! 💪

