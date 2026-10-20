# O que deve ser entregue: Uma classe Animal, com os atributos nome e idade, e o método emitir_som
# Uma classe Cachorro, que herda de Animal e sobrescreve emitir_som
# Uma classe Gato, que herda de Animal e sobrescreve emitir_som
# Um trecho de programa principal que cria um objeto de cada classe, define seus dados e chama emitir_som para os dois

# Requisitos obrigatórios
# O programa precisa ter as três classes (Animal, Cachorro, Gato) estruturadas exatamente com a relação de herança pedida, e cada subclasse deve sobrescrever emitir_som com sua própria mensagem — não é aceito apenas chamar o método herdado sem sobrescrevê-lo. Não é necessário adicionar outros tipos de animais, outros atributos ou outros métodos além dos especificados.

# Passo a passo
# 1. Crie a classe Animal com um construtor (__init__) que recebe e armazena nome e idade.

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# 2. Adicione à classe Animal o método emitir_som, que exibe a mensagem "O animal emitiu um som genérico.".

    def emitir_som(self):
        print("O animal emitiu um som genérico.")

# 3. Crie a classe Cachorro, fazendo com que ela herde de Animal (class Cachorro(Animal):).
# 4. Dentro de Cachorro, defina o método emitir_som novamente, agora exibindo "O cachorro latiu!" — essa nova versão substitui a da classe mãe apenas para objetos do tipo Cachorro.

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro latiu!")

# 5. Repita o processo para a classe Gato, herdando de Animal e sobrescrevendo emitir_som para exibir "O gato miou!".

class Gato(Animal):
    def emitir_som(self):
        print("O gato miou!")

# 6. No programa principal (fora das classes), crie um objeto da classe Cachorro, definindo seu nome e idade.

honey = Cachorro("Honey", 5)

# 7. Crie também um objeto da classe Gato, definindo seu nome e idade.

kitty = Gato("Kitty", 10)

honey.emitir_som()  # Deve exibir: O cachorro latiu!
kitty.emitir_som()  # Deve exibir: O gato miou!

# 8. Chame o método emitir_som para o objeto Cachorro e depois para o objeto Gato, verificando se cada um exibe a mensagem correta e diferente da mensagem genérica da classe Animal.
# 9. Rode o programa e confira na tela se as duas mensagens específicas aparecem corretamente.