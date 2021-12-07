# language: es
Característica: Creación de Examen
  Como creador
  Quiero crear exámenes
  Para evaluar a los estudiantes de un curso

  Antecedentes:
    Dado que existe un curso

  Escenario: Creación de examen exitosa
    Cuando un creador inicia la creación de un examen con titulo "Examen final"
    Y contiene las preguntas:
      | number | text             |
      | 1      | primera pregunta |
      | 2      | segunda pregunta |
    Y publica el examen
    Entonces se creará un nuevo examen

  Escenario: Consulta de exámenes por curso
    Dado que existe un examen
    Cuando se consulta por los exámenes del curso
    Entonces obtengo el detalle de los exámenes del curso

  Escenario: Consulta de exámenes de un curso con ninguno
    Cuando se consulta por los exámenes del curso
    Entonces recibo un mensaje de error

  @wip
  Escenario: Creación de examen fallida
    Cuando un creador inicia la creación de un examen, con el formato que la plataforma le disponibilice, y no complete todos los pasos de manera correcta o exista algun error por parte de la plataforma.
    Entonces se no creará un nuevo examen y se le informará al usuario el error correspondiente
