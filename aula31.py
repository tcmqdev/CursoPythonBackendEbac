# Dado um array meu_arrayzinho contendo n números distintos no internvalo [0, n], retorne o único número no intervalo que está faltando no array.

meu_arrayzinho = [0, 1, 2, 3, 4, 5, 6 , 8, 9, 10]

tamanho_meu_arrayzinho = len(meu_arrayzinho)

soma_valores_meu_arrayzinho = sum(meu_arrayzinho)

soma_total = tamanho_meu_arrayzinho * (tamanho_meu_arrayzinho + 1) // 2

print("O número que está faltando no array é:", soma_total - soma_valores_meu_arrayzinho)  # Saída: O número que está faltando no array é: 1


#meu_arrayzinho = [3, 0, 1]

# 1. Calcular a soma dos números de 0 a n usando a fórmula da soma dos primeiros n números naturais.
#n = len(meu_arrayzinho)

#soma_esperada = n * (n + 1) // 2

# 2. Calcular a soma dos elementos presentes no array.
#soma_atual = sum(meu_arrayzinho)

# 3. O número que está faltando é a diferença entre a soma esperada e a soma atual.
#numero_faltando = soma_esperada - soma_atual

#print("O número que está faltando no array é:", numero_faltando)  # Saída: O número que está faltando no array é: 2
