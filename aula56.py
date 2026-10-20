# for elemento in range(1, 6):
#     print(elemento)

meu_arrayzinho = [elemento for elemento in range(1, 6)]

print(meu_arrayzinho)  # Saída: [1, 2, 3, 4, 5]




palavras = ["python", "é", "divertido"]

iniciais = [palavra[0] for palavra in palavras]

print(iniciais)  # Saída: ['p', 'é', 'd']



quadrados_impares = [elemento**2 for elemento in range(1, 11) if elemento % 2 != 0]
print(quadrados_impares)  # Saída: [1, 9, 25, 49, 81]

#novo_arrayzinho = []

#for elemento in range(1, 11):
#     if elemento % 2 != 0:
#         novo_arrayzinho.append(elemento**2)
#print(novo_arrayzinho)
