Feature: Smoke de PokeAPI
  Como QA necesito validar que el entorno y los pasos funcionan.

  Scenario: GET pokemon por nombre devuelve 200
    When hago GET a "pokemon/pikachu"
    Then la respuesta tiene status 200
    And el header "Content-Type" contiene "application/json"

  Scenario: GET pokemon por id devuelve 200
    When hago GET a "pokemon/25"
    Then la respuesta tiene status 200

  Scenario: Headers importantes presentes
    When hago GET a "pokemon/pikachu"
    Then el header "Content-Type" contiene "application/json"
    And el header "Cache-Control" contiene "public"

  # 1. Happy Path
  Scenario: GET pokemon por nombre devuelve 200 y responde rápido
    When hago GET a "pokemon/pikachu"
    Then la respuesta tiene status 200
    And la respuesta tarda menos de 2.0 segundos
    And el body cumple el schema "pokemon"

  # 2. Boundary Testing - ID mínimo
  Scenario: GET pokemon por id mínimo
    When hago GET a "pokemon/1"
    Then la respuesta tiene status 200
    And el body cumple el schema "pokemon"

  # 2. Boundary Testing - ID máximo
  Scenario: GET pokemon por id máximo
    When hago GET a "pokemon/1010"
    Then la respuesta tiene status 200
    And el body cumple el schema "pokemon"

  # 3. Edge Cases
  Scenario: GET pokemon con nombre inválido devuelve 400 o 404
    When hago GET a "pokemon/!@#invalid"
    Then la respuesta tiene status 400

  # 4. Data Validation
  Scenario: Validar que el JSON contiene campos obligatorios
    When hago GET a "pokemon/pikachu"
    Then el campo "id" es un número mayor que 0
    And el campo "name" es igual a "pikachu"
    And el campo "abilities" es un arreglo no vacío
    And el campo "moves" es un arreglo no vacío
    And el campo "stats" es un arreglo no vacío

  # 5. Response Headers
  Scenario: Validar headers importantes
    When hago GET a "pokemon/pikachu"
    Then el header "Content-Type" contiene "application/json"
    And el header "Cache-Control" contiene "public"
