Feature: Tests endpoint /pokemon/{pokemon}
  Validaciones funcionales, límite y estructura del recurso pokemon.

  Scenario Outline: GET pokemon por nombre - happy path, tiempo y schema
    When hago GET a "pokemon/<name>"
    Then la respuesta tiene status 200
    And la respuesta tarda menos de 2.0 segundos
    And el body cumple el schema "pokemon"

  Examples:
    | name     |
    | pikachu  |
    | mr-mime  |

  Scenario: GET pokemon por id (mínimo válido)
    When hago GET a "pokemon/1"
    Then la respuesta tiene status 200
    And el body cumple el schema "pokemon"

  Scenario: GET pokemon por id fuera de rango devuelve 404
    When hago GET a "pokemon/9999999"
    Then la respuesta tiene status 404

  Scenario: GET pokemon con nombre mal formado devuelve 404
    When hago GET a "pokemon/!@#invalid"
    Then la respuesta tiene status 400

  Scenario: Headers importantes presentes
    When hago GET a "pokemon/pikachu"
    Then el header "Content-Type" contiene "application/json"
