# Reto QA – PokeAPI (Behave + Requests + JSON Schema + Locust)

Automatización BDD para **GET https://pokeapi.co/api/v2/pokemon/{pokemon}** y paginación en **/pokemon?limit&offset**, con validaciones funcionales, de límites, estructura y headers.  
Incluye **smoke suite**, pruebas de **paginación**, y base para **tests de performance con Locust**.

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
├── pokemon_endpoint.feature
├── pokemon_pagination.feature
├── pokemon_smoke.feature
steps/
├── common_steps.py
├── pokemon_steps.py
├── pagination_steps.py
schemas/
└── pokemon.json # schema esperado del recurso /pokemon/{pokemon}
requirements.txt
locustfile.py # (opcional) pruebas de carga contra PokeAPI
mock_server.py # (opcional) servidor local para pruebas controladas

---

## ✅ Casos de Prueba Implementados

El proyecto incluye pruebas automáticas diseñadas para validar el endpoint principal de **PokeAPI**:

### Endpoint:  
`GET https://pokeapi.co/api/v2/pokemon/{pokemon}`

### Escenarios Implementados

1. **Happy Path:**  
   - GET con un Pokémon válido (ej: `pikachu`)  
   - Respuesta con código **200**  
   - Tiempo de respuesta < 2s  
   - Validación de esquema JSON  

2. **Boundary Testing:**  
   - IDs en el límite mínimo (`1`) y máximo (`1010`)  
   - Respuesta con código **200**  
   - Validación de esquema JSON  

3. **Edge Cases:**  
   - Nombres mal formados o con caracteres especiales (ej: `!@#invalid`)  
   - Respuesta con código **400** (Bad Request)  

4. **Data Validation:**  
   - Validación de campos obligatorios: `id`, `name`, `abilities`, `moves`, `stats`  
   - Verificación de tipos de datos (números, strings, arreglos no vacíos)  

5. **Response Headers:**  
   - Validación de headers:  
     - `Content-Type` contiene `application/json`  
     - `Cache-Control` contiene `public`  

---

## 📖 Casos de Paginación y Avanzados

### Endpoint:
`GET https://pokeapi.co/api/v2/pokemon?limit&offset`

### Escenarios Cubiertos
1. Límite por defecto es **20**  
2. `limit=50` devuelve exactamente **50 resultados**  
3. `limit=1 & offset=20` devuelve **1 resultado**  
4. **No se repiten resultados** entre páginas consecutivas (`offset=0` y `offset=20`)  
5. El campo **count** es consistente y mayor a 0  
6. **Limit grande (100)** devuelve 100 resultados  
7. **Offset muy grande (100000)** devuelve lista vacía  
8. Validación de que **todos los nombres listados existen** en el endpoint `/pokemon/{name}`  

---

## ▶️ Ejecución de las pruebas

Para correr todos los escenarios implementados:

```bash
behave
behave features/pokemon_smoke.feature

---

## 🚀 Pruebas de Performance con Locust

Se diseñó un archivo `locustfile.py` con 2 tareas principales:

- `GET /pokemon/pikachu` (peso 3)  
- `GET /pokemon?limit=20&offset=0` (peso 2)  

### Ejecución
Para levantar Locust en modo UI:
```bash
locust -f locustfile.py --host=https://pokeapi.co/api/v2

---

## ▶️ Ejecución de Pruebas

### 1. Contra la PokeAPI real (default)
El entorno ya está configurado para apuntar a **https://pokeapi.co/api/v2**.  
Simplemente ejecuta:

```bash
behave
---

## 📊 Reportes

### Generar reportes JUnit (XML)
```bash
behave --junit --junit-directory reports/
