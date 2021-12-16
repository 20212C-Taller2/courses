# language: es
Característica: Listado de Exámenes
  Como creador o colaborador
  Quiero listar mis exámenes para poder administrarlos

  Antecedentes:
    Dado que existe un curso
    Y un colaborador inscripto
    Y que existe un examen
    Y un estudiante inscripto
    Y resuelve el examen

  Esquema del escenario: Listado de exámenes para creador y colaboradores
    Cuando un "<rol>" lista los exámenes y no selecciona ningún filtro
    Entonces se listarán en pantalla todos los exámenes que ha creado, corregido o debe corregir

    Ejemplos:
      | rol          |
      | creator      |
      | collaborator |

  Esquema del escenario: Listado de exámenes con filtros para creador y colaboradores
    Cuando un "<rol>" lista los exámenes y filtra por el campo "<campo_req>" con el valor "<valor>"
    Entonces se listaran en pantalla todos los exámenes que cumplan el filtro "<campo_res>" con el valor "<valor>"

    Ejemplos:
      | rol          | campo_req  | campo_res | valor               |
      | creator      | student_id | student   | student@example.com |
      | collaborator | exam_id    | exam_id   | 1                   |

  @wip
  Escenario: Listado de examen fallida
    Cuando un creador o colaborador con exámenes asociados ingresa a la pantalla del listado de exámenes y ocurre una falla en el sistema
    Entonces se le informará al usuario el error correspondiente
