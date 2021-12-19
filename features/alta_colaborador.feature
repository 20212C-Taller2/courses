# language: es
Característica: Alta de colaborador en curso
  Como colaborador
  quiero poder participar en distintos cursos,
  pudiendo responder consultas y corregir exámenes.

  Escenario: Alta del rol de colaborador
    Dado que existe un curso
    Cuando su creador asigna al usuario "colaborador@example.com" como colaborador
    Entonces será asignado a cumplir dicha función en el curso

  Escenario: Alta usuario creador como colaborador
    Dado que existe un curso con "creator" "creador@example.com"
    Cuando su creador asigna al usuario "creador@example.com" como colaborador
    Entonces el flujo de inscripción no se completará con error "ERROR_CREATOR_REGISTER"

  Escenario: Inscripción usuario colaborador como estudiante
    Dado que existe un curso
    Cuando el usuario "student@example.com" solicita la inscripción al curso
    Y su creador asigna al usuario "student@example.com" como colaborador
    Entonces el flujo de inscripción no se completará con error "ERROR_STUDENT_REGISTER"

  Escenario: Alta colaborador duplicada
    Dado que existe un curso
    Cuando su creador asigna al usuario "colaborador@example.com" como colaborador por duplicado
    Entonces el flujo de inscripción no se completará con error "ERROR_COLLABORATOR_ALREADY_ENROLLED"
