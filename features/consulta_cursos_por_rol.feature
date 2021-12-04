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

  @wip
  Esquema del escenario: Consulta de Cursos para Estudiante
    Dado que existe un curso
    Y que está inscripto el "<rol>" "<userId>"
    Cuando consulto los cursos a los que está inscripto el "estudiante"

    Ejemplos:
      | rol          | userId                  |
      | student      | estudiante@example.com  |
      | collaborator | colaborador@example.com |
