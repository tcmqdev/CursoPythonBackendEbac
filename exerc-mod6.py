operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]

# Menu numerado gerado com list comprehension
menu = [f"{i + 1} - {operacao}" for i, operacao in enumerate(operacoes)]

# Operações como funções lambda
soma = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y  

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Você deve digitar um número válido. Tente novamente.")

def exibir_menu():
    print("\nEscolha uma operação:")
    for item in menu:
        print(item)

def main():
    while True:  # LOOOP principal da calculadora
        exibir_menu()
        opcao = input("Digite o número da operação desejada: ").strip()

        if opcao not in {"1", "2", "3", "4"}:
            print("Erro: Operação inválida. Por favor, escolha uma opção válida do menu.")
            continue  # volta ao menu, sem perguntar "outra operação?"

        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")

        if opcao == "1":
            print(f"Resultado da soma: {soma(num1, num2)}")
        elif opcao == "2":
            print(f"Resultado da subtração: {subtracao(num1, num2)}")
        elif opcao == "3":
            print(f"Resultado da multiplicação: {multiplicacao(num1, num2)}")
        elif opcao == "4":
            # Repete a pergunta do divisor até ele ser diferente de zero
            while num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                num2 = obter_numero("Digite o segundo número (não pode ser zero): ")
            print(f"Resultado da divisão: {divisao(num1, num2)}")

        continuar = input("\nDeseja realizar outra operação? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando o programa. Obrigado por usar a calculadora!")
            break  # encerra o loop principal 

if __name__ == "__main__":
    main()