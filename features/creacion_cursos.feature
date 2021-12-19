# language: es
Característica: Creación de curso
  Como creador
  Quiero poder crear un curso
  Para que realicen los estudiantes que se inscriban al mismo y poder obtener o no ganancias por esto.

  Escenario: Creación Exitosa
    Dado que un creador realiza un nuevo curso con:
      | key          | value                 |
      | title        | titulo                |
      | description  | Descripción del curso |
      | subscription | free                  |
      | type         | WEB_DEVELOPMENT       |
      | creator      | profesor@example.com  |
      | location     | Buenos Aires          |
    Y tiene asociados los hashtags asociados:
      | name       |
      | desarrollo |
      | software   |
    Y tiene las URL de multimedia asociadas:
      | url              |
      | ruta/del/archivo |
    Cuando lo crea
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
    Entonces el sistema deberá informarle que no es una operación permitida

    Ejemplos:
      | campo        |
      | title        |
      | subscription |
      | type         |
      | creator      |

  Escenario: Consulta de tipos de cursos
    Cuando consulto los tipos de cursos que ofrece la plataforma
    Entonces recibo una lista con los distintos tipos de cursos

  Escenario: Creación de curso con usuario inexistente
    Dado que el id de usuario "creator@example.com" no existe
    Cuando intenta crear un curso
    Entonces el sistema deberá informar el error con código "CREATOR_NOT_FOUND"
