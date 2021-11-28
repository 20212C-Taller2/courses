# language: es
Característica: Alta de colaborador en curso
  Como colaborador
  quiero poder participar en distintos cursos,
  pudiendo responder consultas y corregir exámenes.

  Escenario: Alta del rol de colaborador
    Dado que existe un curso
    Cuando su creador asigna al usuario "colaborador@example.com" como colaborador
    Entonces será asignado a cumplir dicha función en el curso
