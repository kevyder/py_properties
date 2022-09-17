# py_properties

## Dependecias / Tecnologias

- **[poetry](https://python-poetry.org/)**
- **[http](https://docs.python.org/3/library/http.server.html#)** module
- **[pytest](https://docs.pytest.org/en/stable/)**
- **[mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/)**
- **[pre-commit](https://pre-commit.com/)**

## Información del proyecto

- Se utilizará el modulo http para hacer funcionar un servidor http.
    + La configuracion del servidor estará en el archivo `app/server.py`
- Se utilizará la libreria mysql connector para python para tener acceso a la base de datos.
    + La configuracion de conexion a la base de datos estará en el archivo `app/db_config.py`
    + En los casos dónde existan ids de propiedades duplicados se traerá la primer propiedad creada y se obviaran las demás.
    + Se excluiran las propiedades que no contengan dirección.
- Se usará pre-commit para tener un control más estricto del estandar pep8 y el orden de llamado de dependencias.
- las variables del entorno estarán en el archivo `.env` el cual estará excluido del repositorio por razones de seguridad.
