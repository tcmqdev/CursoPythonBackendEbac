# Receba um número e determine se ele é um palíndromo (lê-se da mesma forma de frente para trás e de trás para frente).

# 1. Receber um número do usuário
numero = input("Digite um número: ")

# 2. Verificar se o número é um palíndromo
if numero == numero[::-1]:
    print(f"O número {numero} é um palíndromo.")
else:
    print(f"O número {numero} não é um palíndromo.")
