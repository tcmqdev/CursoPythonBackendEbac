# Dado um arry de inteiros meu_arrayzinho, um inteiro sortudo é um inteiro que tem uma frequência no array igual ao seu valor:

meu_arrayzinho = [2, 2, 3, 4]

# 1. Criar um dicionário para contar a frequência de cada elemento no array.
meu_dicionariozinho = {}
for i in meu_arrayzinho:
    if i not in meu_dicionariozinho:
        meu_dicionariozinho[i] = 1
    else:
        meu_dicionariozinho[i] += 1

# 2. Encontrar os inteiros sortudos, ou seja, aqueles que têm uma frequência igual ao seu valor.
inteiros_sortudos = []

for chave, valor in meu_dicionariozinho.items():
    if chave == valor:
        inteiros_sortudos.append(chave)

print("Os inteiros sortudos são:", inteiros_sortudos)  # Saída: Os inteiros sortudos são: [2]
