# Soma de 1 a N: Receba um número N e exiba a soma de todos os números de 1 até N.

# 1. Receber um número N do usuário
N = int(input("Digite um número: "))

# 2. Calcular a soma de 1 até N
soma = 0
for i in range(1, N + 1):
    soma += i

# 3. Exibir o resultado
print(f"A soma de 1 até {N} é: {soma}")