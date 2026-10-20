#try:
#    print('oi')
#except:
#    print('tchau')

#try:
#    resultado = 10 / 0  # Isso vai gerar uma exceção de divisão por zero
#except ZeroDivisionError:
#    print("Erro: Divisão por zero não é permitida.")


try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(resultado)
except ValueError:
    print("Erro: Você deve digitar um número inteiro válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")