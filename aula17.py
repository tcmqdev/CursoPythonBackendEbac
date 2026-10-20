# Escreva um programa que receba três números e exiba o segundo maior número entre eles.

# Preciso receber três números do usuário

numero1, numero2, numero3 = map(int, input().split())  # Recebendo três números do usuário e convertendo para inteiros

#Criar uma lógica para ver quem é o segundo maior número entre eles
#Encontrando o segundo maior número
#if numero1 >= numero2 and numero1 >= numero3:
#    if numero2 >= numero3:
#        print(numero2)
#    else:
#        print(numero3)
#elif numero2 >= numero1 and numero2 >= numero3:
#   if numero1 >= numero3:
#        print(numero1)
#    else:
#        print(numero3)
#else:
#    if numero1 >= numero2:
#        print(numero1)
#    else:
#        print(numero2)

#Outra forma de encontrar o segundo maior número é usando a função sorted() para ordenar os números e pegar o segundo elemento da lista ordenada
#numeros = [numero1, numero2, numero3]  # Criando uma lista
#numeros.sort(reverse=True)  # Ordenando a lista em ordem decrescente
#print(numeros[1])  # Imprimindo o segundo elemento da lista ordenada

#Outra forma de encontrar o segundo maior número é usando a função max() para encontrar o maior número e depois removê-lo da lista e encontrar o maior número novamente
#numeros = [numero1, numero2, numero3]  # Criando uma lista
#maior = max(numeros)
#numeros.remove(maior)
#segundo_maior = max(numeros)
#print(segundo_maior)

#Exemplo da aula
meu_array = []

meu_array.append(numero1)
meu_array.append(numero2)
meu_array.append(numero3)

meu_array.sort()

#print(meu_array)
print(meu_array[1])  # Imprimindo o segundo maior número
