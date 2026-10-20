# Dado um array de números inteiros, retorne a soma do menor número e do maior número do array.

meu_arrayzinho = [1, 5, 33, 8, 77, 43, 124, 6, 8, 99]

## Aula

# 1. Vamos ordenar o array para deixar o menor valor na posição zero e o maior valor na última posição do array.
meu_arrayzinho.sort()

# 2. Efetuar a soma do valor da primeira posição com o valor da última posição do array.
soma = meu_arrayzinho[0] + meu_arrayzinho[-1]

print("A soma do menor e do maior número é:", soma)  # Saída: A soma do menor e do maior número é: 125


# 1. Encontrar o menor e o maior número do array.
#menor_numero = min(meu_arrayzinho)
#maior_numero = max(meu_arrayzinho)

# 2. Calcular a soma do menor e do maior número.
#soma = menor_numero + maior_numero

#print("A soma do menor e do maior número é:", soma)  # Saída: A soma do menor e do maior número é: 125
