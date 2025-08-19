Feature: Escenarios avanzados de Paginación y Validación de PokeAPI
  Validar comportamientos con límites grandes, offsets fuera de rango y consistencia de datos.

  Scenario: Limit de 100 devuelve 100 resultados
    When hago GET a "pokemon?limit=100"
    Then la respuesta tiene status 200
    And la longitud de "results" es 100

  Scenario: Offset muy grande devuelve resultados vacíos
    When hago GET a "pokemon?limit=20&offset=100000"
    Then la respuesta tiene status 200
    And la longitud de "results" es 0

  Scenario: Validar que nombres devueltos en paginación existen en el endpoint individual
    When guardo los nombres de "results" de "pokemon?limit=5&offset=0" como "sample_names"
    Then cada nombre en "sample_names" existe en el endpoint pokemon
