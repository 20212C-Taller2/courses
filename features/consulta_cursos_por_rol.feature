# language: es
Característica: Consulta de Cursos por Rol
  Como usuario
  Quiero consultar los cursos para los cuales soy creador, estudiante y colaborador
  Para obtener la información más detallada

  Escenario: Consulta de Cursos para Creador
    Dado que existe un curso con "creator" "creador@example.com"
    Y que existe un curso con "creator" "otro_creador@example.com"
    Cuando consulto los cursos del "creator" "creador@example.com"
    Entonces obtengo los cursos que le pertenecen al "creator"

  Esquema del escenario: Consulta de Cursos por Rol
    Dado que existe un curso
    Y que está inscripto el "<rol>" "<userId>"
    Cuando consulto los cursos a los que está inscripto el "<rol>" "<userId>"
    Entonces obtengo los cursos a los cuales está inscripto el "<rol>" "<userId>"

    Ejemplos:
      | rol           | userId                  |
      | students      | estudiante@example.com  |
      | collaborators | colaborador@example.com |

  Esquema del escenario: Consulta de Cursos por Rol sin resultados
    Dado que existe un curso
    Y el "<userId>" no se encuentra inscripto como "<rol>"
    Cuando consulto los cursos a los que está inscripto el "<rol>" "<userId>"
    Entonces se deberá notificar al usuario que no existen resultados para su búsqueda

    Ejemplos:
      | rol           | userId                  |
      | students      | estudiante@example.com  |
      | collaborators | colaborador@example.com |
