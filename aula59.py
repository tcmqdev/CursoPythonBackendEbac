# Funções Lambda

# def soma(x, y):
#     return x + y
# print(soma(3, 5))

#soma = lambda x, y: x + y
#print(soma(3, 5))


meu_arrayzinho = [1, 2, 3, 4, 5]

duplicados = map(lambda x: x * 2, meu_arrayzinho)

print(list(duplicados))  # Converte o resultado para uma lista e imprime