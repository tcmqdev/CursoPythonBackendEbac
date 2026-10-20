# Par ou Ímpar: Receba um número e exiba se ele é par ou ímpar.

# 1. Receber um número do usuário
numero = int(input("Digite um número: "))

# 2. Verificar se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

# 3. Exibir o resultado para o usuário

print("Obrigado por usar o programa!")