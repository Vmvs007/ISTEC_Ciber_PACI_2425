atletas = {
    "Cristiano Ronaldo": {"desporto": "Futebol", "pais": "Portugal"},
    "Usain Bolt": {"desporto": "Atletismo", "pais": "Jamaica"},
    "Simone Biles": {"desporto": "Ginástica", "pais": "EUA"},
    "Pepe": {"desporto": "Futebol", "pais": "Portugal"},
    "Messi": {"desporto": "Futebol", "pais": "Argentina"},
}

opcao = -1

while (opcao != 0):
    print("\n_______________ GESTÃO DE ATLETAS _______________")
    print("1. NOVO ATLETA")
    print("2. ATUALIZAR ATLETA")
    print("3. LISTAR POR DESPORTO")
    print("4. LISTAR POR PAÍS")
    print("5. LISTAR COMPLETO")
    print("0. SAIR\n")

    opcao = int(input("Insira a sua opção: "))

    if (opcao == 1):
        print("\n_______________ NOVO ATLETA _______________")
        novoNome = input("Nome: ")

        if novoNome not in atletas:  # o atleta é mesmo novo
            novoDesporto = input("Desporto: ")
            novoPais = input("País: ")

            atletas[novoNome] = {"desporto": novoDesporto, "pais": novoPais}

        else:  # atleta já existe
            print("\nAtleta já existente")


    elif (opcao == 2):
        print("\n_______________ ATUALIZAR ATLETA _______________")
        atualizarNome = input("Nome: ")

        if atualizarNome in atletas:  # atleta existe

            atualizarDesporto = input("Desporto: ")
            atualizarPais = input("País: ")

            atletas[atualizarNome] = {"desporto": atualizarDesporto, "pais": atualizarPais}

        else:  # atleta não encontrado
            print("\nAtleta não reconhecido")

    elif (opcao == 3):
        print("\n_______________ LISTAR POR DESPORTO _______________")

        desportoPesquisa = input("Desporto: ")
        encontrado = False

        print(f"\n_______________ {desportoPesquisa} _______________")
        for nomeAtleta, infoAtleta in atletas.items():
            if (infoAtleta["desporto"] == desportoPesquisa):
                print(f"{nomeAtleta} | País: {infoAtleta["pais"]}")
                encontrado=True


        if(encontrado==False):
            print("Sem atletas neste desporto")

    elif (opcao == 4):
        print("\n_______________ LISTAR POR PAÍS _______________")

        paisPesquisa = input("País: ")
        encontrado = False

        print(f"\n_______________ {paisPesquisa} _______________")
        for nomeAtleta, infoAtleta in atletas.items():
            if (infoAtleta["pais"] == paisPesquisa):
                print(f"{nomeAtleta} | Desporto: {infoAtleta["desporto"]}")
                encontrado=True

        if(encontrado==False):
            print("Sem atletas neste país")

    elif (opcao == 5):
        print("\n_______________ LISTAR COMPLETO _______________")

        for nomeAtleta, infoAtleta in atletas.items():
            print(f"{nomeAtleta} | Desporto: {infoAtleta["desporto"]} | País: {infoAtleta["pais"]}")

    elif (opcao == 0):
        print("\n_______________ SAIR _______________")
        print("Obrigado. Até à próxima!")

    else:
        print("\n_______________ OPÇÃO INVÁLIDA _______________")
