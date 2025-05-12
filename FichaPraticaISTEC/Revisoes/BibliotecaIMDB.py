def limparConsola():
    for i in range(100):
        print()


def loginAdministrador():
    print("__________ Login __________")
    username = input("Username: ")
    password = input("Password: ")

    if (username == "IMDV" and password == "123456"):
        return True

    # Login Inválido
    return False


def menuInicial(dicionarioFilmes):
    opcaoLogin = 1

    while (opcaoLogin != 0):

        print("\n****************** Bem-vind@ ao IMDB ******************")
        print("1. Cliente")
        print("2. Administrador")

        opcaoLogin = int(input("Tipo de Acesso (0 para sair): "))

        limparConsola()

        match (opcaoLogin):
            case 1:  # Cliente
                limparConsola()
                menuCliente(dicionarioFilmes)

            case 2:  # Administrador
                if (loginAdministrador()):
                    limparConsola()
                    menuAdministrador(dicionarioFilmes)
                else:
                    print("Login Incorreto...")

            case 0:  # Sair
                print("Encerrar o programa...")

            case _:  # Opção Inválida
                print("Opção não reconhecida...")


def menuCliente(dicionarioFilmes):
    opcaoCliente = 1

    while (opcaoCliente != 0):
        print("\n****************** IMDB: Cliente ******************")
        print("1. Listar Todos os Filmes")
        print("2. Consultar Filme")
        print("3. Melhor Filme")
        print("4. Pior Filme")
        print("5. Pesquisar Filmes - Diretor")
        print("6. Pesquisar Filmes - Categoria")

        opcaoCliente = int(input("Selecione a sua opção (0 para voltar): "))

        limparConsola()

        match (opcaoCliente):
            case 1:
                print("__________ Listar Todos os Filmes __________")
                imprimirDicionario(dicionarioFilmes)

            case 2:
                print("__________ Consultar Filme __________")
                filmePesquisar = input("Nome do Filme: ")
                pesquisarFilme(dicionarioFilmes, filmePesquisar)

            case 3:
                print("__________ Melhor Filme __________")

            case 4:
                print("__________ Pior Filme __________")

            case 5:
                print("__________ Pesquisar Filmes - Diretor __________")
                diretorPesquisar = input("Diretor: ")
                # filmesDiretor(dicionarioFilmes,diretorPesquisar)
                filmesPesquisarParametro(dicionarioFilmes, "diretor", diretorPesquisar)

            case 6:
                print("__________ Pesquisar Filmes - Categoria __________")
                categoriaPesquisar = input("Categoria: ")
                filmesCategoria(dicionarioFilmes, categoriaPesquisar)

            case 0:
                print()

            case _:  # Opção Inválida
                print("Opção não reconhecida...")


def menuAdministrador(dicionarioFilmes):
    opcaoAdministrador = 1

    while (opcaoAdministrador != 0):
        print("\n****************** IMDB: Administrador ******************")
        print("1. Novo Filme")
        print("2. Atualizar Classificação de um Filme")

        opcaoAdministrador = int(input("Selecione a sua opção (0 para voltar): "))

        limparConsola()

        match (opcaoAdministrador):
            case 1:
                print("__________ Novo Filme __________")

            case 2:
                print("__________ Atualizar Classificação de um Filme __________")

            case 0:
                print()

            case _:  # Opção Inválida
                print("Opção não reconhecida...")


def pesquisarFilme(dicionarioFilmes, filmePesquisar):
    if filmePesquisar in dicionarioFilmes:  # Existe filme
        # Imprimir informação
        imprimirFilme(dicionarioFilmes, filmePesquisar)

    else:  # Não existe
        print("Filme não encontrado...")


def imprimirDicionario(dicionarioFilmes):
    for nomeFilme, infoFilme in dicionarioFilmes.items():
        imprimirFilme(dicionarioFilmes, nomeFilme)


def filmesDiretor(dicionarioFilmes, diretorPesquisar):
    for nomeFilme, infoFilme in dicionarioFilmes.items():
        if (infoFilme["diretor"] == diretorPesquisar):  # Filme do Diretor
            imprimirFilme(dicionarioFilmes, nomeFilme)


def filmesCategoria(dicionarioFilmes, categoriaPesquisar):
    for nomeFilme, infoFilme in dicionarioFilmes.items():
        if (infoFilme["categoria"] == categoriaPesquisar):  # Filme da Categoria
            imprimirFilme(dicionarioFilmes, nomeFilme)


def filmesPesquisarParametro(dicionarioFilmes, fatorPesquisa, valorPesquisa):
    for nomeFilme, infoFilme in dicionarioFilmes.items():
        if (infoFilme[fatorPesquisa] == valorPesquisa):
            imprimirFilme(dicionarioFilmes, nomeFilme)


def imprimirFilme(dicionarioFilmes, nomeFilme):
    print(f"\n--- {nomeFilme} ---")
    print(f"\tDiretor: {dicionarioFilmes[nomeFilme]["diretor"]}")
    print(f"\tAno: {dicionarioFilmes[nomeFilme]["ano"]}")
    print(f"\tCategoria: {dicionarioFilmes[nomeFilme]["categoria"]}")
    print(f"\tAvaliação: {dicionarioFilmes[nomeFilme]["avaliacao"]}")
