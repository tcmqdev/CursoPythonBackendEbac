# Molde do Pokemon, com vários atributos

# Classe é o molde que vamos usar para criar Pokemons diferentes, com características diferentes, mas que compartilham o mesmo padrão.

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
        print(f"Altura do {self.nome}: {self.altura}")

    def mostrar_peso_pokemon(self):
        print(f"Peso do {self.nome}: {self.peso}\n")

# Chegou a hora de pegar a classe e de fato construir essas coisas. Por enquanto só temos o molde, mas ainda não temos nenhum Pokemon de verdade.
# Construir dentro da orientação a objetos é o mesmo que construir um objeto a partir de um molde. O molde é a classe, e o objeto é a instância da classe.

pikachu = MoldePokemon("Pikachu", 400, "Elétrico", "Choque do Trovão", "50 cm", "15 kg")
charizard = MoldePokemon("Charizard", 500, "Fogo", "Lança chamas", "2 m", "1500 Kg")
miau = MoldePokemon("Miau", 100, "Normal", "Unhada", "50 cm", "15 kg")

pikachu.mostrar_nome_pokemon()
pikachu.mostrar_altura_pokemon()
pikachu.mostrar_peso_pokemon()

charizard.mostrar_nome_pokemon()
charizard.mostrar_altura_pokemon()
charizard.mostrar_peso_pokemon()

miau.mostrar_nome_pokemon()
miau.mostrar_altura_pokemon()
miau.mostrar_peso_pokemon()