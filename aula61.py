class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo!")

#animal = Animal("Cachorro")

#animal.comer()  # Saída: Cachorro está comendo!


class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} está latindo: au au!")

meu_cachorrinho = Cachorro("Goku")

meu_cachorrinho.comer()  # Saída: Goku está comendo!
meu_cachorrinho.latir()  # Saída: Goku está latindo: au au!