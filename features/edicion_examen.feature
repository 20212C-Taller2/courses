# language: es
Característica: Edición de examen
  Como creador
  Quiero editar exámenes previamente a estar publicado

  Antecedentes:
    Dado que existe un curso
    Y un creador inicia la creación de un examen con titulo "Examen a editar"
    Y contiene las preguntas:
      | number | text             |
      | 1      | primera pregunta |
      | 2      | segunda pregunta |
    Y publica el examen

  Escenario: Edición de examen exitosa con misma cantidad de preguntas
    Cuando un creador edite el titulo por "Examen editado"
    Y edite las preguntas:
      | number | text                     |
      | 1      | primera pregunta editada |
      | 2      | segunda pregunta editada |
    Entonces el examen será actualizado con esta nueva información

  Escenario: Edición de examen exitosa con menor cantidad de preguntas
    Cuando un creador edite el titulo por "Examen editado"
    Y edite las preguntas:
      | number | text                     |
      | 1      | primera pregunta editada |
    Entonces el examen será actualizado con esta nueva información

  Escenario: Edición de examen exitosa con mayor cantidad de preguntas
    Cuando un creador edite el titulo por "Examen editado"
    Y edite las preguntas:
      | number | text                     |
      | 1      | primera pregunta editada |
      | 2      | segunda pregunta editada |
      | 3      | tercera pregunta nueva   |
    Entonces el examen será actualizado con esta nueva información

  @wip
  Escenario: Edición de examen fallida
    Cuando un creador edite los datos/información de un examen no publicado de manera incorrecta o exista alguna falla en el sistema
    Entonces no se editará el examen y se le informará al usuario el error correspondiente
