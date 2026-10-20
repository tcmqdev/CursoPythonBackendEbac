# Dado um array de números inteiros, retorne quantos deles contém um número par de dígitos.
nums = [12, 345, 2, 6, 7896]

# novo_array = ["12", "345", "2", "6", "7896"]
# 1. Criar um novo array de strings que vai ter os mesmos valores do primeiro array, porém como strings

novo_array = [str(num) for num in nums]

# 2. Fazer um looping dentro do novo_array para fazer a verificação de números com dígitos pares
# 3. Fazer a contagem e mostrar (printar) na tela o resultado.

count = 0

for i in novo_array:
    if len(i) % 2 == 0:
        count += 1

print(count)

# 1. Receber a lista de números inteiros como entrada.

#nums = [12, 345, 2, 6, 7896]

# 2. Inicializar uma variável para contar os números com dígitos pares.
# 3. Iterar sobre cada número na lista.

#count = 0

#for num in nums:

    # 4. Converter o número em string e verificar o comprimento da string.

#    if len(str(num)) % 2 == 0:

        # 5. Se o comprimento for par, incrementar a contagem.

#        count += 1

# 6. Retornar a contagem final.

#print(count)    
