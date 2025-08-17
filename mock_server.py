# mock_server.py -- servidor mínimo para pruebas de carga
from flask import Flask, jsonify, request, abort
import re

app = Flask(__name__)

# crear lista de ejemplo de 200 pokemons (incluye pikachu y mr-mime)
POKEMON = []
for i in range(1, 201):
    name = f"pokemon{i}"
    if i == 1:
        name = "bulbasaur"
    if i == 25:
        name = "pikachu"
    if i == 122:
        name = "mr-mime"
    POKEMON.append({
        "id": i,
        "name": name,
        "height": 1,
        "weight": 1,
        "abilities": [{"ability": {"name": "run"}}],
        "types": [{"type": {"name": "normal"}}],
        "moves": [],
        "stats": []
    })

def is_malformed(identifier: str) -> bool:
    # aceptar letras, números y guion. Si hay otros chars, considerarlo mal formado.
    return not re.match(r'^[a-z0-9-]+$', identifier.lower())

@app.route("/pokemon")
def list_pokemon():
    try:
        limit = int(request.args.get("limit", 20))
    except:
        limit = 20
    try:
        offset = int(request.args.get("offset", 0))
    except:
        offset = 0
    total = len(POKEMON)
    results = [{"name": p["name"]} for p in POKEMON[offset: offset + limit]]
    next_url = None
    prev_url = None
    return jsonify({
        "count": total,
        "results": results,
        "next": next_url,
        "previous": prev_url
    }), 200

@app.route("/pokemon/<identifier>")
def get_pokemon(identifier):
    # mal formado -> 400
    if is_malformed(identifier):
        return "Bad Request", 400
    # si es dígito, buscar por id
    if identifier.isdigit():
        pid = int(identifier)
        for p in POKEMON:
            if p["id"] == pid:
                return jsonify(p), 200
        return "Not Found", 404
    # buscar por nombre
    for p in POKEMON:
        if p["name"].lower() == identifier.lower():
            return jsonify(p), 200
    return "Not Found", 404

if __name__ == "__main__":
    # instalar flask si no lo tienes: pip install flask
    app.run(host="0.0.0.0", port=8000, debug=False)
