# Tabuada: Receba um número e exiba a tabuada desse número de 1 a 10.

# 1. Receber um número do usuário
numero = float(input("Digite um número para ver a tabuada: "))

# 2. Exibir a tabuada do número de 1 a 10
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

print("Obrigado por usar o programa!")