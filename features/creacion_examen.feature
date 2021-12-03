# language: es
Característica: Creación de Examen
  Como creador
  Quiero crear exámenes
  Para evaluar a los estudiantes de un curso

  Antecedentes:
    Dado que existe un curso con "exams" "1"

  Escenario: Creación de examen exitosa
    Cuando un creador inicia la creación de un examen con titulo "Examen final"
    Y contiene las preguntas:
      | number | text             |
      | 1      | primera pregunta |
      | 2      | segunda pregunta |
    Y publica el examen
    Entonces se creará un nuevo examen

  @wip
  Escenario: Publicación de examen
    Cuando un creador quiera publicar un examen previamente creado.
    Entonces el examen estara disponible para que los estudiantes lo rindan.

  @wip
  Escenario: Creación de examen fallida
    Cuando un creador inicia la creación de un examen, con el formato que la plataforma le disponibilice, y no complete todos los pasos de manera correcta o exista algun error por parte de la plataforma.
    Entonces se no creará un nuevo examen y se le informará al usuario el error correspondiente
