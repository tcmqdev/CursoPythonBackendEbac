# Decorators: coloca mais atributos no objeto, sem precisar alterar a função original

def meu_decorator(func):
    def wrapper():
        print("Antes da execução da função.")
        func()
        print("Depois da execução da função.")
    return wrapper

@meu_decorator
def despedida():
    print("Adeus!")


@meu_decorator
def saudacao():
    print("Olá!")

saudacao()  # Chamada da função saudacao
despedida()  # Chamada da função despedida