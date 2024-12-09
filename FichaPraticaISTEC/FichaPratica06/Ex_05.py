lista_compras = {}

opcao = 0

while True:
    print("\nMenu:")
    print("1. Adicionar produto")
    print("2. Calcular preço total")
    print("3. Mostrar lista de compras")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_produto = input("Insira o nome do produto: ")
        preco_produto = float(input("Insira o preço do produto: "))
        lista_compras[nome_produto] = preco_produto
        print(f"Produto '{nome_produto}' adicionado com sucesso!")

    elif opcao == "2":
        if lista_compras:
            preco_total = sum(lista_compras.values())
            print(f"O preço total dos produtos é: €{preco_total:.2f}")
        else:
            print("A lista de compras está vazia.")

    elif opcao == "3":
        if lista_compras:
            print("\nLista de Compras:")
            for produto, preco in lista_compras.items():
                print(f"- {produto}: €{preco:.2f}")
        else:
            print("A lista de compras está vazia.")

    elif opcao == "4":
        print("Encerrando o programa. Até logo!")


    else:
        print("Opção inválida. Tente novamente.")
