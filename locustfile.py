from locust import HttpUser, task, between

class PokeApiUser(HttpUser):
    wait_time = between(1, 3)  # Espera entre 1 y 3 segundos entre requests

    @task(3)  # Peso 3: se ejecuta más veces
    def get_pokemon_by_name(self):
        self.client.get("/pokemon/pikachu")

    @task(2)  # Peso 2: se ejecuta menos que el anterior
    def get_pokemon_list(self):
        self.client.get("/pokemon?limit=20&offset=0")
