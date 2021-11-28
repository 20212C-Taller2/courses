# language: es
Característica: Inscripción a Curso
  Como estudiante
  quiero poder seleccionar un curso
  para así poder acceder a sus contenidos y evaluaciones

  Antecedentes:
    Dado que existe un curso

  Escenario: Inscripción exitosa
    Cuando el usuario "alumno@dominio.com" solicita la inscripción a un curso
    Entonces se deberá ejecutar el flujo correspondiente para establecer dicha inscripción.

  @wip
  Escenario: Inscripción fallida
    Cuando se rechacen las condiciones para la inscripción a la suscripción o el sistema rechaza su inscripción.
    Entonces no se deberá el flujo de inscripción en el curso
