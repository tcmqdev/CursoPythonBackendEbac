# Receba uma lista de palavras e ordene-as em ordem alfabética.

# 1. Receber uma lista de palavras do usuário
palavras = input("Digite uma lista de palavras separadas por vírgula: ").split(', ')

# 2. Ordenar a lista de palavras em ordem alfabética
palavras_ordenadas = sorted(palavras)

# 3. Exibir a lista ordenada
print("Lista de palavras em ordem alfabética:")
for palavra in palavras_ordenadas:
    print(palavra.strip())

# Exemplo da aula:

# meu_array = []
# for i in range(5):
#     palavra = input("Digite uma palavra: ")
#     meu_array.append(palavra)

# meu_array.sort()