# language: es
Característica: Búsqueda de Cursos
  Como estudiante
  quiero poder realizar búsquedas de cursos por sus atributos
  para visualizar los cursos y así poder obtener más información sobre los mismos.

  Escenario: Búsqueda de curso por categorias
    Dado que existen cursos con tipo:
      | type            |
      | WEB_DEVELOPMENT |
      | GRAPHIC_DESIGN  |
    Cuando se realiza una búsqueda utilizando un filtrado por categoria "WEB_DEVELOPMENT"
    Entonces se retornan los cursos que cumplan dichos filtros.

  @wip
  Escenario: Búsqueda sin resultados
    Cuando se realiza una búsqueda utilizando un filtrado y no existen cursos que cumplan tal condición
    Entonces se deberá notificar al usuario que no existen resultados para su búsqueda.
