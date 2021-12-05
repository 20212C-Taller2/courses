# language: es
Característica: Edición de curso
  Como creador
  Quiero poder modificar un curso
  Para actualizar su contenido

  Esquema del escenario: Edición de datos exitosa
    Dado que existe un curso con "<nombre_campo>" "<valor>"
    Cuando su creador realice la edición del campo "<nombre_campo>" con el valor "<nuevo_valor>"
    Entonces al confirmar los nuevos cambios, el campo "<nombre_campo>" se verá reflejado en el curso con el valor "<nuevo_valor>"

    Ejemplos:
      | nombre_campo | valor           | nuevo_valor       |
      | title        | titulo          | nuevo titulo      |
      | description  | descripcion     | nueva descripcion |
      | type         | WEB_DEVELOPMENT | GRAPHIC_DESIGN    |

  Esquema del escenario: Edición de datos fallida
    Dado que existe un curso
    Cuando su creador realice la edición del campo "<nombre_campo>" con el valor "<valor_invalido>"
    Entonces el sistema deberá informarle que no es una operación permitida

    Ejemplos:
      | nombre_campo | valor_invalido |
      | type         | invalid        |
