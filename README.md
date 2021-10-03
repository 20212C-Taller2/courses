# python-fastapi
Esta version base de pruebas integra: 

vunicorn con FastApi + Postgres para recuperar items insertados en una base de datos. 

El modelo incluye: 
- Organizacion basica del proyecto
- Operaciones crud (dp/crud.py) y modelos de base de datos (models.py) 
- Uso de dependencias para asegurar una sesion con la base por request
- Esquemas de validacion de datos con pydantic (schemas.py)
- Routers independientes por dominio (/routers)
- Dockerfile para crear e instalar imagen (sin config de env variables por ahora)
- Migraciones automaticas de la BD (Yes!) con alembic

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

## DB migrations
Antes de iniciar el server de desarrollorealizar las migraciones pendientes con `alembic upgrade head`.

Si se quiere crear una nueva revision usar `alembic revision --autogenerate -m "some message"`. Luego validar que el 
archivo generado satisfaga correctamente los cambios realizados

## Ejecucion
Iniciar el server con:
```shell
vunicorn app.main:app

## Tip: Si se esta desarrollando utilizar para auto reload del server ante cambios
vunicorn app.main:app --reload
```

