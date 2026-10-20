# Objetivo: Implementar um sistema de classes para modelar animais com seus sons característicos e desenvolver testes unitários para verificar o comportamento esperado de cada classe

# Classe Base Animal:
# Deve ter um construtor que receba nome (string) e idade (inteiro)
# Deve possuir um método emitir_som() que imprime:
# "O animal emitiu um som genérico."

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("O animal emitiu um som genérico.")


# Classe Derivada Cachorro:
# Deve herdar da classe Animal
# Deve sobrescrever o método emitir_som() para imprimir:
# "O cachorro latiu!"

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro latiu!")


# Classe Derivada Gato:
# Deve herdar da classe Animal
# Deve sobrescrever o método emitir_som() para imprimir:
# "O gato miou!"

class Gato(Animal):
    def emitir_som(self):
        print("O gato miou!")

