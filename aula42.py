# Uma classe é um molde - Usamos este molde para construir coisas que queremos que tem um mesmo padrão, mas que podem ter características diferentes.

# - Nome
# - HP
# - Tipo
# - Ataque
# - Altura
# - Peso

# - Nome -> Pikachu
# - HP -> 300
# - Tipo -> Eletrico
# - Ataque -> Choque do Trovão
# - Altura -> 50 cm
# - Peso -> 15 kg

# - Nome -> Charizard
# - HP -> 450
# - Tipo -> Fogo
# - Ataque -> Lança chamas
# - Altura -> 2 m
# - Peso -> 1500 Kg

class MoldePokemon:
    def __init__(self, nome, hp, tipo, ataque, altura, peso):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        self.altura = altura
        self.peso = peso

    def mostrar_nome_pokemon(self):
        print(f"Nome do Pokemon: {self.nome}")

    def mostrar_altura_pokemon(self):
        print(f"Altura do Pokemon: {self.altura}")

    def mostrar_peso_pokemon(self):
        print(f"Peso do Pokemon: {self.peso}")