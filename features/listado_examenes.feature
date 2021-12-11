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

  @wip
  Escenario: Listado de exámenes para creador
    Cuando un creador lista los exámenes y no selecciona ningún filtro
    Entonces se listarán en pantalla todos los exámenes que ha creado, corregido o debe corregir

  @wip
  Escenario: Listado de exámenes con filtros para creador
    Cuando un creador lista los exámenes y selecciona algún filtro
    Entonces se listaran en pantalla todos los exámenes que cumplan dicho filtro

  @wip
  Escenario: Listado de exámenes para colaborador
    Cuando un colaborador lista los exámenes y no selecciona ningún filtro
    Entonces se listaran en pantalla todos los exámenes que ha corregido o debe corregir

  @wip
  Escenario: Listado de exámenes con filtros para colaborador
    Cuando un colaborador lista los exámenes y no selecciona algun filtro
    Entonces se listaran en pantalla todos los exámenes que cumplan dicho filtro

  @wip
  Escenario: Listado de examen fallida
    Cuando un creador o colaborador con exámenes asociados ingresa a la pantalla del listado de exámenes y ocurre una falla en el sistema
    Entonces se le informará al usuario el error correspondiente
