# language: es
Característica: Búsqueda de Cursos por Suscripción
  Como estudiante
  quiero poder realizar búsquedas de cursos por tipo de suscripción
  para visualizar los cursos y así poder obtener más información sobre el mismo.

  Escenario: Filtrado etapa
    Dado que existen cursos con suscripción:
      | subscription |
      | free         |
    Cuando se realiza una búsqueda utilizando como filtro el tipo de suscripción de un curso "free"
    Entonces se retornan los cursos que cumplan dicha suscripción

  Escenario: Búsqueda sin resultados
    Cuando se realiza una búsqueda por suscripción utilizando un filtrado y no existen cursos que cumplan tal condición
    Entonces se deberá notificar al usuario que no existen resultados para su búsqueda
