# language: es
Característica: Desinscripción a curso
  Como estudiante
  Quiero poder desinscribirme de un curso
  Para así no acceder a sus contenidos y evaluaciones.

  Antecedentes:
    Dado que existe un curso
    Y el usuario "alumno@example.com" se encuentra inscripto

  Escenario: Desinscripción exitosa
    Cuando solicita la desinscripción a un curso
    Entonces se deberá ejecutar el flujo correspondiente para establecer dicha desinscripción.

  @wip
  Escenario: Desinscripción fallida
    Y que transcurrió un día desde su inscripción
    Cuando solicita la desinscripción a un curso
    Entonces el flujo de desinscripción no se completará con el error "ERROR_UNENROLLMENT_DATE_OVERDUE"
