# Polimorfismo é a capacidade de um objeto se comportar de diferentes formas dependendo do contexto. 
# Em Python, isso é frequentemente implementado através de métodos que podem ser sobrescritos em subclasses.

class Animal:
    def falar(self):
        pass  # Método genérico, será sobrescrito nas subclasses

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau, miau!"


animais = [Cachorro(), Gato()]
for animal in animais:
    print(animal.falar())