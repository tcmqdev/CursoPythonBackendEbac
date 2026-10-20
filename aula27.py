# Você recebe um array de núymeros inteiros meu_arrayzinho.
# Os elementos únicos de um array são os elementos que aparecem exatamente uma vez no array.
# Retorne a soma de todos os elementos úicos de meu_arrayzinho.

meu_arrayzinho = [1, 2, 3, 3, 2, 4, 5, 5, 7, 6, 6]

# 1. Criar um dicionário para encontrar a chave e o valor.

meu_dicionariozinho = {}

for i in meu_arrayzinho:
    if i not in meu_dicionariozinho:
        meu_dicionariozinho[i] = 1
    else:
        meu_dicionariozinho[i] += 1

# 2. Encontrar quem são os valores que aparecem uma única vez.
# 3. Fazer a soma das chaves que aparecem apenas uma vez.

soma_das_chaves = 0

for chave, valor in meu_dicionariozinho.items():
    if valor == 1:
        soma_das_chaves += chave

print("A soma dos elementos únicos é:", soma_das_chaves)  # Saída: A soma dos elementos únicos é: 12


#def soma_elementos_unicos(meu_arrayzinho):
    # 1. Criar um dicionário para contar a frequência de cada elemento no array.
#    frequencia = {}
    
    # 2. Iterar sobre cada elemento no array e atualizar a contagem no dicionário.
#    for num in meu_arrayzinho:
#        if num in frequencia:
#            frequencia[num] += 1
#        else:
#            frequencia[num] = 1
    
    # 3. Inicializar uma variável para armazenar a soma dos elementos únicos.
#    soma_unicos = 0
    
    # 4. Iterar sobre o dicionário de frequência e somar os elementos que aparecem exatamente uma vez.
#    for num, count in frequencia.items():
#        if count == 1:
#            soma_unicos += num
    
    # 5. Retornar a soma dos elementos únicos.
#    return soma_unicos
# Exemplo de uso:
#meu_arrayzinho = [1, 2, 3, 2, 4, 5, 5]
#resultado = soma_elementos_unicos(meu_arrayzinho)
#print("A soma dos elementos únicos é:", resultado)  # Saída: A soma dos elementos únicos é: 8

