# language: es
Característica: Creación de curso
  Como creador
  Quiero poder crear un curso
  Para que realicen los estudiantes que se inscriban al mismo y poder obtener o no ganancias por esto.

  Escenario: Creación Exitosa
    Cuando un creador realice un nuevo curso con:
      | key          | value                 |
      | title        | titulo                |
      | description  | Descripción del curso |
      | exams        | 1                     |
      | subscription | free                  |
#     | creator      | usuario               |
#     | tags             | Hashtags asociados para facilitar la búsqueda.                               |
#     | type             | Se deberá elegir un tipo de curso dentro de los permitidos por la plataforma |
#     | Fotos y/o videos | Material multimedia que acompañe                                             |
#     | location         | Ubicación geografica del curso                                               |
    Entonces recibo el curso creado correctamente


  Escenario: Consulta de curso
    Dado que existe un curso
    Cuando lo consulto
    Entonces este curso podrá ser visualizado y realizado por los estudiantes.

  Escenario: Consulta de curso inexistente
    Cuando consulto un curso que no existe
    Entonces recibo un mensaje de error

  Esquema del escenario: Creación de curso con información insuficiente
    Cuando un creador realice un nuevo curso con "<campo>" faltante.
    Entonces el sistema deberá informarle que no es una operación permitida.

    Ejemplos:
      | campo        |
      | title        |
      | exams        |
      | subscription |

  Escenario: Consulta de tipos de suscripciones
    Cuando consulto las suscripciones
    Entonces recibo una lista con los distintos tipos de suscripciones
