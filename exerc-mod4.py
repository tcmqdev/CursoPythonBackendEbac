# construir um programa de terminal para gerenciar o estoque de produtos de um comércio genérico, sem necessidade de inventar uma marca ou cenário de negócio.

# Um programa Python com um menu funcional (adicionar produto, listar produtos, remover produto, atualizar quantidade, sair)
# Os dados dos produtos armazenados em um dicionário, seguindo exatamente a estrutura pedida
# Código organizado em funções, uma para cada funcionalidade do menu

# Requisitos obrigatórios
# O programa precisa usar um dicionário (não listas separadas) para armazenar os dados dos produtos, ter cada funcionalidade do menu implementada como uma função própria, ordenar a listagem de produtos alfabeticamente usando uma função lambda, e rodar em loop contínuo até a opção de sair ser escolhida. Não é necessário persistir os dados em arquivo ou banco de dados — o estoque pode existir apenas durante a execução do programa.

# 1. Crie um dicionário vazio para armazenar os produtos, onde cada chave será o nome do produto e o valor será outro dicionário com as chaves "quantidade" e "preço".

produtos = {}

# 2. Escreva uma função para exibir o menu com as opções: adicionar produto, listar produtos, remover produto, atualizar quantidade de produto e sair.

def exibir_menu():
    print("\n=== Menu ===")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Remover produto")
    print("4. Atualizar quantidade de produto")
    print("5. Sair")

# 3. Crie uma função para adicionar produto: ela deve pedir nome, quantidade e preço, e guardar essas informações no dicionário.

def adicionar_produto():
    nome = input("\nNome do produto: ")
    quantidade = int(input("Quantidade: "))
    preço = float(input("Preço: "))
    
    produtos[nome] = {"quantidade": quantidade, "preço": preço}

# 4. Crie uma função para listar produtos: ela deve exibir cada produto no formato Nome do produto: Quantidade disponível - Preço, ordenados em ordem alfabética (use sorted() com uma função lambda como chave de ordenação).

def listar_produtos():
    for nome, info in sorted(produtos.items(), key=lambda x: x[0]):
        print(f"\n{nome}: {info['quantidade']} - R${info['preço']:.2f}")

# 5. Crie uma função para remover produto: ela deve pedir o nome do produto e verificar se ele existe no dicionário antes de remover. Se não existir, exiba uma mensagem de erro.

def remover_produto():
    nome = input("Nome do produto a ser removido: ")
    if nome in produtos:
        del produtos[nome]
        print(f"\nProduto '{nome}' removido com sucesso.")
    else:
        print(f"\nProduto '{nome}' não encontrado.")

# 6. Crie uma função para atualizar a quantidade de um produto: ela deve pedir o nome do produto e a nova quantidade, atualizando o dicionário se o produto existir, ou exibindo erro caso contrário.

def atualizar_quantidade():
    nome = input("Nome do produto: ")
    if nome in produtos:
        nova_quantidade = int(input("Nova quantidade: "))
        produtos[nome]["quantidade"] = nova_quantidade
        print(f"\nQuantidade do produto '{nome}' atualizada com sucesso.")
    else:
        print(f"\nProduto '{nome}' não encontrado.")

# 7. Monte o loop principal do programa: ele deve mostrar o menu, capturar a escolha do usuário com input(), chamar a função correspondente e repetir até que o usuário escolha sair.

while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_produto()
    elif escolha == "2":
        listar_produtos()
    elif escolha == "3":
        remover_produto()
    elif escolha == "4":
        atualizar_quantidade()
    elif escolha == "5":
        print("\nSaindo...")
        break
    else:
        print("\nOpção inválida. Tente novamente.")

# 8. Teste cada uma das opções do menu, incluindo os casos de erro (remover ou atualizar um produto que não existe).
# 9. Revise se a listagem de produtos está realmente sendo ordenada em ordem alfabética antes de considerar o exercício concluído.