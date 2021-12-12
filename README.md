# API Cursos

Repositorio para la API Rest de Cursos de Ubademy

Desarrollada con Python y FastAPI

Esta version base de pruebas integra:

vunicorn con FastApi + Postgres para recuperar items insertados en una base de datos.

El modelo incluye:

- Organizacion basica del proyecto
- Operaciones crud (`db/crud.py`) y modelos de base de datos (`models.py`)
- Uso de dependencias para asegurar una sesion con la base por _request_
- Esquemas de validación de datos con `pydantic` (`schemas.py`)
- Routers independientes por dominio (`/routers`)
- Dockerización de ambiente (servidor y base de datos) para desarrollo con `docker-compose`

## Environment

Requiere las siguientes variables de entorno:

```shell
export FASTAPI_POSTGRESQL=postgresql+psycopg2://user:pass@databaseurl/db
```

## Install

Necesita Python +3.7 instalado (testeado con 3.8.11 en mi maquina) para correr con `pip`.

Ejecutar:

```shell
pip install -r requirements.txt
pre-commit install
alembic upgrade head
```

## Migraciones

Antes de iniciar el server de desarrollo realizar las migraciones pendientes con `alembic upgrade head`.

Si se quiere crear una nueva revision usar `alembic revision --autogenerate -m "<message>"`. Luego validar que el
archivo generado satisfaga correctamente los cambios realizados

## Ejecución

Iniciar el server con:

```shell
vunicorn app.main:app

## Tip: Si se esta desarrollando utilizar para auto reload del server ante cambios
vunicorn app.main:app --reload
```

## Desarrollo con Docker

Construir la imagen y ejecutar el container:

```shell
$ docker-compose up -d --build
```

Detener el contenedor:

```shell
$ docker-compose stop
```

Ejecutar contenedor:

```shell
$ docker-compose start
```

Detener container y eliminar imagen:

```shell
$ docker-compose down
```

## Ejecución tests

- Unitarios:`$ python -m pytest tests`
- Integración: `$ behave`

### Cobertura 

- Reporte: `$ coverage run -m pytest tests/ && coverage run -a -m behave && coverage report -m`
- HTML: `$ coverage html`
