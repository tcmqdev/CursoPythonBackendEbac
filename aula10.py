gato = 10
# a variável gato recebe o número inteiro 10
cachorro = 5.5
# a variável cachorro recebe o número decimal 5.5
peixe = "o peixe é lindo"
# a variável peixe recebe a string "o peixe é lindo"
dinossauro = 10

# Primeira estrutura -> ==
# Segunda estrutura -> !=
# Terceira estrutura -> <=
# Quarta estrutura -> >=
# Quinta estrutura -> >
# Sexta estrutura -> <
# Sétima estrutura -> and
# Oitava estrutura -> or

if gato == 10:
    print("Gato é 10 mesmo!")

if cachorro != 6:
    print("O cachorro não é 6!")

if cachorro < gato:
    print("O cachorro é menor que o gato!")
else:
    print("O cachorro não é menor que o gato!")

if cachorro > gato:
    print("O cachorro é maior que o gato!")
else:
    print("O cachorro não é maior que o gato!")

if gato == dinossauro:
    print("O gato é igual ao dinossauro!")

if gato <= dinossauro:
    print("O gato é menor ou igual ao dinossauro!")

if gato >= dinossauro:
    print("O gato é maior ou igual ao dinossauro!")

if peixe <= "o peixe é lindo":
    print("O peixe é menor ou igual!")

if gato >= 10:
    print("O gato é maior ou igual a 10!")

if cachorro > 5:
    print("O cachorro é maior que 5!")

if peixe < "o peixe é feio":
    print("O peixe é menor que 'o peixe é feio'!")