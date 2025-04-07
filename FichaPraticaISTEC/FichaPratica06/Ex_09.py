catalogo = {
    "Laptop HP 15": [0, 900],
    "Frigorifico Samsung": [0, 1500],
    "Torradeira Philips": [0, 55],
    "Microondas Bosch": [0, 150]
}

opcao = 1

while (opcao != 0):
    print("\n********** Gestão de Vendas **********")
    print("1. Nova Venda")
    print("2. Total Vendas de um Produto")
    print("3. Total Vendas")
    print("4. Lista Todas os Produtos")
    print("0. Sair\n")
    opcao = int(input("Insira a sua opção: "))

    if (opcao == 1):
        print("\n********** Nova Venda **********")
        produto = input("Produto: ")
        quantidadeVendida = int(input("Quantidade: "))

        if produto in catalogo:
            catalogo[produto][0] += quantidadeVendida
        else:
            valorUnitario = float(input("Valor Unitário: "))
            catalogo[produto] = [quantidadeVendida, valorUnitario]

    elif (opcao == 2):
        print("\n********** Total Vendas de um Produto **********")

        produto = input("Produto: ")
        print(f"{catalogo[produto][0] * catalogo[produto][1]} €")


    elif (opcao == 3):

        print("\n********** Total Vendas **********")

        totalVendas = 0
        for produtoAtual in catalogo:
            totalVendas += catalogo[produtoAtual][0] * catalogo[produtoAtual][1]

        print(f"{totalVendas} €")

    elif (opcao == 4):
        print("\n********** Produtos **********")
        for produtoAtual in catalogo:
            print(
                f"{produtoAtual} | Quant. Vendida: {catalogo[produtoAtual][0]} | Valor Uni.: {catalogo[produtoAtual][1]}€")


    elif (opcao == 0):
        print("\n********** Sair **********")
        print("Obrigado. Até à próxima!")


    else:
        print("\n********** Opção Inválida **********")
