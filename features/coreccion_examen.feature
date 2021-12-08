# language: es
Característica: Corrección de examen
  Como creador o colaborador
  Quiero corregir exámenes
  Para evaluar el conocimiento de los estudiantes que rindan el examen

  Antecedentes:
    Dado que existe un curso
    Y un colaborador inscripto
    Y que existe un examen
    Y un estudiante inscripto
    Y resuelve el examen

  Esquema del escenario: Corrección de examen exitosa
    Cuando el "<rol>" "<userId>" realiza la corrección de un examen de manera correcta
    Entonces el examen pasará a un estado finalizado y tendrá una nota asociada

    Ejemplos:
      | rol          | userId                   |
      | creator      | creator@example.com      |
      | collaborator | collaborator@example.com |

  @wip
  Esquema del escenario: Corrección de examen fallida
    Cuando el "<rol>" "<userId>" inicia la corrección de un examen
    Y esta no finaliza de manera correcta
    Entonces se no corregirá el examen y se le informará al usuario el error correspondiente

    Ejemplos:
      | rol          | userId                   |
      | creator      | creator@example.com      |
      | collaborator | collaborator@example.com |
