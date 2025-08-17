# Reto QA – PokeAPI (Behave + Requests + JSON Schema + Locust)

Automatización BDD para **GET https://pokeapi.co/api/v2/pokemon/{pokemon}** y paginación en **/pokemon?limit&offset**, con validaciones funcionales, límite, estructura y headers. Incluye smoke suite y base para pruebas de performance con Locust.

---

## 🧩 Stack
- Python 3.10+  
- Behave (BDD)  
- Requests  
- jsonschema  
- Locust (opcional, performance)

---

## 📁 Estructura del proyecto
features/
pokemon_endpoint.feature
pokemon_pagination.feature
pokemon_smoke.feature
steps/
common_steps.py
pokemon_steps.py
pagination_steps.py
schemas/
pokemon.json # schema esperado del recurso /pokemon/{pokemon}
requirements.txt
locustfile.py # (opcional) pruebas de carga contra PokeAPI
mock_server.py # (opcional) servidor local para pruebas controladas
