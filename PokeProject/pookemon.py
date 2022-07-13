import requests
class Poketest:
    def __init__(self,nome):
        self.nome = nome
        #Requisição pra pokeapi
        self.reqi = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.nome}')
        reqi_json = self.reqi.json()

        self.art_work = reqi_json['sprites']['other']['official-artwork']['front_default']
        self.pokemon_id = reqi_json['id']
        self.pokemon_altura = reqi_json['height']
        self.pokemon_peso = reqi_json['weight']
        self.pokemon_tipos = reqi_json['types']
