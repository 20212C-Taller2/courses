# language: es
Característica: Completar Examen
  Como estudiante
  Quiero completar un examen
  Para poder así verificar mis conocimientos y aprobar

  Antecedentes:
    Dado que existe un curso
    Y que existe un examen
    Y un estudiante inscripto

  Escenario: Examen completado de manera exitosa
    Cuando el estudiante completa un examen de manera exitosa
    Entonces se enviará el examen para su corrección
    Y el estudiante no podrá completarlo nuevamente

  @wip
  Escenario: Examen completado con errores
    Cuando un estudiante no completa un examen de manera exitosa debido a que ocurre un error en el sistema
    Entonces el estudiante no podrá completarlo nuevamente y se enviará el examen para su revisión
