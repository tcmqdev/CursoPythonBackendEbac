# Objetivo: Desenvolver um programa em Python para gerenciar o estoque de produtos, permitindo adicionar, listar, remover e atualizar produtos através de um menu interativo.
# Estrutura de Dados:
# Utilize um dicionário para armazenar os produtos, onde:
# Chave: Nome do produto (string)
# Valor: Outro dicionário com:
# {
#     "quantidade": int,  # Quantidade em estoque
#     "preço": float      # Preço unitário
# }
# Funções a Serem Implementadas:
# adicionar_produto(estoque)
# Solicita: nome, quantidade e preço do produto
# Verifica se o produto já existe
# Adiciona ao estoque se for novo
# listar_produtos(estoque)
# remover_produto(estoque)
# Remove um produto pelo nome
# Mensagens:
# Sucesso: "Produto 'X' removido com sucesso!"
# Erro: "Erro: Produto não encontrado."
# atualizar_quantidade(estoque)
# Modifica a quantidade de um produto existente
# exibir_menu()
# Mostra as opções:
# 1 - Adicionar produto  
# 2 - Listar produtos  
# 3 - Remover produto  
# 4 - Atualizar quantidade  
# 5 - Sair  
# Função Principal (main)
# Controla o fluxo do programa
# Repete o menu até que o usuário escolha sair

def adicionar_produto(estoque, nome, quantidade, preço):
    nome = nome.strip()
    if nome in estoque:
        return "Erro: Produto já cadastrado."
    else:
        estoque[nome] = {"quantidade": quantidade, "preço": preço}
        return f"Produto '{nome}' adicionado com sucesso!"

def listar_produtos(estoque):
    if not estoque:
        return "Nenhum produto cadastrado."
    else:
        resultado = ["Lista de produtos:"]
        for nome, info in sorted(estoque.items(), key=lambda x: x[0]):
            resultado.append(f"{nome}: Quantidade disponível - {info['quantidade']} | Preço - R${info['preço']:.2f}")
        return "\n".join(resultado)

def remover_produto(estoque, nome):
    nome = nome.strip()
    if nome in estoque:
        del estoque[nome]
        return f"Produto '{nome}' removido com sucesso!"
    else:
        return "Erro: Produto não encontrado."

def atualizar_quantidade(estoque, nome, nova_quantidade):
    nome = nome.strip()
    if nome in estoque:
        estoque[nome]["quantidade"] = nova_quantidade
        return f"Quantidade do produto '{nome}' atualizada para {nova_quantidade}."
    else:
        return "Erro: Produto não encontrado."

def exibir_menu():
    return (
        "\n=== Menu ===\n"
        "1 - Adicionar produto\n"
        "2 - Listar produtos\n"
        "3 - Remover produto\n"
        "4 - Atualizar quantidade\n"
        "5 - Sair"
    )

def main():
    estoque = {}
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            print(adicionar_produto(estoque, nome, quantidade, preco))
        elif opcao == "2":
            print(listar_produtos(estoque))
        elif opcao == "3":
            nome = input("Nome do produto a ser removido ")
            print(remover_produto(estoque, nome))
        elif opcao == "4":
            nome = input("Nome do produto: ")
            nova_qtd = int(input("Nova quantidade: "))
            print(atualizar_quantidade(estoque, nome, nova_qtd))
        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()