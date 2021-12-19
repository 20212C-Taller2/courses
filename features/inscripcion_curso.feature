# language: es
Característica: Inscripción a Curso
  Como estudiante
  quiero poder seleccionar un curso
  para así poder acceder a sus contenidos y evaluaciones

  Escenario: Inscripción exitosa
    Dado que existe un curso
    Cuando el usuario "alumno@example.com" solicita la inscripción al curso
    Entonces se deberá ejecutar el flujo correspondiente para establecer dicha inscripción.

  @wip
  Escenario: Inscripción fallida
    Cuando se rechacen las condiciones para la inscripción a la suscripción o el sistema rechaza su inscripción.
    Entonces no se deberá completa el flujo de inscripción en el curso

  Escenario: Inscripción usuario creador como estudiante
    Dado que existe un curso con "creator" "creador@example.com"
    Cuando el usuario "creador@example.com" solicita la inscripción al curso
    Entonces el flujo de inscripción no se completará con error "ERROR_CREATOR_STUDENT_ENROLL"

  Escenario: Inscripción usuario colaborador como estudiante
    Dado que existe un curso
    Cuando su creador asigna al usuario "collaborator@example.com" como colaborador
    Y el usuario "collaborator@example.com" solicita la inscripción al curso
    Entonces el flujo de inscripción no se completará con error "ERROR_COLLABORATOR_STUDENT_ENROLL"

  Escenario: Inscripción duplicada
    Dado que existe un curso
    Cuando el usuario "alumno@example.com" solicita la inscripción al curso por duplicado
    Entonces el flujo de inscripción no se completará con error "ERROR_STUDENT_ALREADY_ENROLLED"
