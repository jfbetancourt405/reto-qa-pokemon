Feature: Paginación en /pokemon?limit&offset
  Validar el comportamiento de paginación, límites y consistencia de datos.

  Scenario: Límite por defecto es 20
    When hago GET a "pokemon"
    Then la respuesta tiene status 200
    And la longitud de "results" es 20

  Scenario: Limit de 50 devuelve 50 resultados
    When hago GET a "pokemon?limit=50"
    Then la respuesta tiene status 200
    And la longitud de "results" es 50

  Scenario: Limit de 1 y offset 20 devuelve un único resultado
    When hago GET a "pokemon?limit=1&offset=20"
    Then la respuesta tiene status 200
    And la longitud de "results" es 1

  Scenario: Paginación no repite resultados entre páginas consecutivas
    When guardo los nombres de "results" de "pokemon?limit=20&offset=0" como "page1"
    And guardo los nombres de "results" de "pokemon?limit=20&offset=20" como "page2"
    Then no hay elementos duplicados entre "page1" y "page2"

  Scenario: El campo count es consistente
    When hago GET a "pokemon?limit=20"
    Then el campo "count" es un número mayor que 0
