# Dado um array com números inteiros, cada elemento aparece duas vezes, exceto um. Encontre aquele único.

meu_arrayzinho = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

# 1. Criar um dicionário para adicionar os valores do array através de chave - valor, ou seja, a chave sendo o valor do array e o valor sendo a quantidade de vezes que a chave aparece.
meudicionariozinho = {}
for i in meu_arrayzinho:
    if i not in meudicionariozinho:
        meudicionariozinho[i] = 1
    else:
        meudicionariozinho[i] += 1

# 2. Encontrar o elemento que aparece apenas uma vez.

for chave, valor in meudicionariozinho.items():
    if valor == 1:

        print(chave)
