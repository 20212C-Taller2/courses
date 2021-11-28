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
    Cuando se rechacen las condiciones para la desinscripción a la suscripción o el sistema rechaza su desinscripción.
    Entonces no se deberá el flujo de desinscripción en el curso
