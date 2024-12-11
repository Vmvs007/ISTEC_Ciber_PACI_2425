listaContactos = []

opcao = 1

while (opcao != 0):

    print("\n********** Contactos **********")
    print("1. Adicionar Novo Contacto")
    print("2. Atualizar Contacto")
    print("3. Excluir Contacto")
    print("4. Lista Contactos")
    print("5. Limpar Todos Contactos")
    print("0. Sair")
    opcao = int(input("Insira a sua opção: "))

    print()
    if (opcao == 1):  # Adicionar Novo Contacto
        print("********** Adicionar Contacto **********")

        novoContacto = {}
        novoContacto["nome"] = input("Nome: ")
        novoContacto["telefone"] = input("Telefone: ")
        novoContacto["email"] = input("Email: ")
        novoContacto["cidade"] = input("Cidade: ")

        listaContactos.append(novoContacto)

    elif (opcao == 2):  # Atualizar Contacto
        nomePesquisa = input("Nome do Contacto a Atualizar: ")

        for i in range(0, len(listaContactos)):
            if (listaContactos[i]["nome"] == nomePesquisa):
                listaContactos[i]["telefone"] = input("Telefone: ")
                listaContactos[i]["email"] = input("Email: ")
                listaContactos[i]["cidade"] = input("Cidade: ")

    elif (opcao == 3):  # Excluir Contacto

        nomePesquisa = input("Nome do Contacto a Atualizar: ")

        for i in range(0, len(listaContactos)):
            if (listaContactos[i]["nome"] == nomePesquisa):
                listaContactos.pop(i)

        print()
    elif (opcao == 4):  # Listar Contactos

        for i in range(0, len(listaContactos)):
            print(
                f"Nome: {listaContactos[i]["nome"]} | Telefone: {listaContactos[i]["telefone"]} | Email: {listaContactos[i]["email"]} | Cidade: {listaContactos[i]["cidade"]}")

        print()

    elif (opcao == 5):  # Limpar Contactos

        listaContactos = []

    elif (opcao == 0):  # Sair
        print()
    else:
        print("Opção Inválida")
