import json

def totalVendas(dadosVendas):
    total = 0

    for venda in dadosVendas:
        total += venda["quantidade_vendida"]*venda["preco_unitario"]

    return total

def menuCliente(dadosVendas):
    opcao=1

    while(opcao!=0):
        print("***** MENU CLIENTE *****")
        print("1. Consultar Produtos")
        print("2. Pesquisar por Categoria")
        print("3. Produto Mais Barato e Mais Caro")
        print("0. Voltar")

        opcao=int(input("Opção: "))

        match(opcao):
            case 1:
                print("___ Consultar Produtos ___")

            case 2:
                print("___ Pesquisar por Categoria ___")

            case 3:
                print("___ Produto Mais Barato e Mais Caro ___")

            case 0:
                print("___ Voltar ___")

            case _:
                print("Opção não reconhecida...")



def menuAdmin(dadosVendas):
    opcao = 1

    while (opcao != 0):
        print("***** MENU ADMINISTRADOR *****")
        print("1. Produto Mais Vendido - Unidades")
        print("2. Produto Mais Vendido - Valor")
        print("3. Melhor Venda - Unidades")
        print("4. Melhor Venda - Valor")
        print("5. Total Vendas")
        print("6. Média Vendas")
        print("0. Voltar")

        opcao = int(input("Opção: "))

        match (opcao):
            case 1:
                print("___ Produto Mais Vendido - Unidades ___")

            case 2:
                print("___ Produto Mais Vendido - Valor ___")

            case 3:
                print("___ Melhor Venda - Unidades ___")

            case 4:
                print("___ Melhor Venda - Valor ___")

            case 5:
                print("___ Total Vendas ___")
                print(totalVendas(dadosVendas)+"€")

            case 6:
                print("___ Médias Vendas ___")

            case 0:
                print("___ Voltar ___")

            case _:
                print("Opção não reconhecida...")


def menuFuncionario(dadosVendas):
    opcao = 1

    while (opcao != 0):
        print("***** MENU FUNCIONÁRIO *****")
        print("1. Nova Venda")
        print("0. Voltar")

        opcao = int(input("Opção: "))

        match (opcao):
            case 1:
                print("___ Nova Venda ___")

            case 0:
                print("___ Voltar ___")

            case _:
                print("Opção não reconhecida...")

    return dadosVendas


def menuInicial(dadosLogin, dadosVendas):
    opcao = 1

    while (opcao != 0):
        print("\n***** Programa Minimercado Grandes Negócios *****")
        print("1. Cliente")
        print("2. Staff")
        print("0. Sair")

        opcao = int(input("Opção:"))

        match (opcao):
            case 1:  # Cliente
                menuCliente(dadosVendas)

            case 2:  # Staff

                usernameInput = input("Username: ")
                passwordInput = input("Password: ")

                tipoAcesso = validarAcessos(dadosLogin,usernameInput,passwordInput)

                match (tipoAcesso):
                    case "ADMIN":
                        menuAdmin(dadosVendas)

                    case "FUNC":
                        dadosVendas = menuFuncionario(dadosVendas)

                    case "ERRO":
                        print("Acessos inválidos!")

            case 0:
                print("Encerrar o programa...")

            case _:
                print("Opção não reconhecida...")

    return dadosVendas


def validarAcessos(dadosLogin, usernameInput, passwordInput):
    for acesso in dadosLogin:

        if (usernameInput == acesso["utilizador"] and passwordInput == acesso["password"]):
            return acesso["tipo_conta"]

    return "ERRO"


def carregar_dados(caminho):
    dados = {}
    with open(caminho, 'r') as ficheiro:
        dados = json.load(ficheiro)

    return dados


def guardar_dados(caminho, dados):
    with open(caminho, 'w') as ficheiro:
        json.dump(dados, ficheiro, indent=4)


if __name__ == "__main__":
    caminhoFicheiroLogins = "../Ficheiros/login_grandesNegocios.json"
    caminhoFicheiroVendas = "../Ficheiros/minimercado.json"

    dadosLogin = carregar_dados(caminhoFicheiroLogins)
    dadosVendas = carregar_dados(caminhoFicheiroVendas)

    dadosVendas = menuInicial(dadosLogin, dadosVendas)

    guardar_dados("../Ficheiros/minimercado.json", dadosVendas)
