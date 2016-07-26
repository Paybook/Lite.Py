
# Paybook Python Lite

### Requerimientos

1. [Python 2.7.6](https://www.python.org/downloads/)
2. Instalar dependencias ```pip install -r requirements.txt```
3. Un API Key de Paybook

### Descripción:

Este es un proyecto que muestra como construir una aplicación de backend en Python haciendo uso del framework Flask. La aplicación tiene la siguientes características:

1. Integración completa con el API Rest de Paybook a través de la librería de Paybook para Python [sync-py](https://github.com/Paybook/sync-py)
2. Cuenta con los endpoints básicos para que tu puedas construir a partir de estos tu propia aplicación, reciclándolos, o bien, agregando tus propios endpoints.
3. Cuenta con una conexión a una base de datos SQL a través del gestor [sqlite3](http://www.tutorialspoint.com/sqlite/sqlite_python.htm)
4. Conexión directa con [Lite-Frontend-React](https://github.com/Paybook/lite-frontend-react)
5. Contiene las siguientes funcionalidades: registro de usuarios, inicio de sesión, registro y borrado de credenciales de instituciones, consulta de transacciones e integración con el widget de Paybook.

A continuación se muestra un diagrama con la arquitectura del proyecto:

![Diagrama](https://github.com/Paybook/lite-python/blob/master/lite_python_diagram.png "Diagrama")


### Ejecución:

Clonar el proyecto en tu equipo

```
$ git clone https://github.com/Paybook/lite-python.git
```

Entrar al directiorio del proyecto

```
$ cd lite-python
```

Ejecutar el proyecto pasando como parámetro tu API Key de Paybook:

```
$ python main.py -a YOUR_PAYBOOK_API_KEY
```

Puedes acceder a la aplicación de React por medio de tu navegador:

```
http://localhost:5000/
```

En una nueva terminal puedes checar los registros de ejecución (logs). Estos se encuentran en el archivo app.log ubicado en el directorio de lite-python (el archivo se creará automáticamente una vez que sea ejecutado el programa, si el archivo ya existe utilizará el existente). Puedes visualizarlo constantemente para checar las peticiones que se hacen a la aplicación en backend:

```
$ tail -f app.log
```

La base de datos se almacenará en el archivo paybook.db ubicado en el directorio de lite-python (este archivo, al igual que el archivo de logs, se creará automáticamente una vez que sea ejecutado el programa, si el archivo ya existe utilizará el existente). Para visualizar las tablas y los registros de la base de datos se recomienda usar [DB Browser for SQLite](http://sqlitebrowser.org/). Aquí lo único que tienes que hacer es cargar el archivo paybook.db desde la interfaz del DB Browser y con esto tendrás accesso a la base de datos del proyecto.












































