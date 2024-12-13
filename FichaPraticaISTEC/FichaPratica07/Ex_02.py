taxasCambio = {"USD": 1.0,
               "EUR": 0.85,
               "BRL": 5.25,
               "MEX_PESO": 20.15,
               "FIL_PESO": 58.04,
               "GBP": 0.78
               }


usernameCorreto = "admin"
passwordCorreta = "123456"
opcaoLogin = -1

while (opcaoLogin != 0):
    print("\n********** TAXAS DE CÂMBIO **********")
    print("1. ADMIN")
    print("2. CLIENTE")
    print("0. SAIR\n")

    opcaoLogin = int(input("Insira a opção: "))
    print()

    if (opcaoLogin == 1):  # ADMIN

        print("\n********** TAXAS DE CÂMBIO - LOGIN ADMIN **********")
        username = input("Username: ")
        password = input("Password: ")

        if (username == usernameCorreto and password == passwordCorreta):  # Login válido

            opcaoAdmin = -1
            while (opcaoAdmin != 0):

                print("\n********** TAXAS DE CÂMBIO - ADMIN **********")
                print("1. ATUALIZAR CÂMBIOS")
                print("2. NOVA MOEDA")
                print("3. ALTERAR PASSWORD")
                print("0. VOLTAR\n")

                opcaoAdmin = int(input("Insira a opção: "))
                print()
                if (opcaoAdmin == 1):
                    print("********** ATUALIZAR CÂMBIOS **********")
                    moedaAtualizar = input("Moeda a Atualizar: ")

                    if (moedaAtualizar in taxasCambio):  # Moeda a atualizar existe
                        novaTaxa = float(input("Nova Taxa: "))

                        taxasCambio[moedaAtualizar] = novaTaxa

                        print(f"{moedaAtualizar} atualizado para: {novaTaxa}")
                    else:
                        print("Moeda não reconhecida")

                elif (opcaoAdmin == 2):
                    print("********** NOVA MOEDA **********")

                    moedaNova = input("Moeda Nova: ")

                    if (moedaNova not in taxasCambio):
                        taxaMoedaNova = float(input(f"Taxa {moedaNova}: "))
                        taxasCambio[moedaNova] = taxaMoedaNova
                    else:
                        print("Moeda existente")

                elif (opcaoAdmin == 3):
                    print("********** ALTERAR PASSWORD **********")
                    passwordCorreta = input("Nova Password: ")

                elif (opcaoAdmin == 0):
                    print()

                else:
                    print("********** OPÇÃO INVÁLIDA **********")

        else:  # Login inválido
            print("\nAcesso negado")

    elif (opcaoLogin == 2):  # CLIENTE

        opcaoCliente = -1
        while (opcaoCliente != 0):
            print("\n********** TAXAS DE CÂMBIO - CLIENTE **********")
            print("1. CONSULTAR CÂMBIOS")
            print("2. CAMBIAR MOEDAS")
            print("0. VOLTAR\n")

            opcaoCliente = int(input("Insira a opção: "))
            print()

            if (opcaoCliente == 1):
                print("********** CONSULTAR CÂMBIOS **********")

                for moeda, taxa in taxasCambio.items():
                    print(f"{moeda}: {taxa}")


            elif (opcaoCliente == 2):
                print("********** CAMBIAR MOEDAS **********")
                valorOriginal = float(input("Valor: "))
                moedaOriginal = input("Moeda Original: ")

                if (moedaOriginal in taxasCambio):  # Moeda original existe

                    moedaDestino = input("Moeda Destino: ")

                    if (moedaDestino in taxasCambio):  # Moeda destino existe

                        valorConvertido = (valorOriginal * taxasCambio[moedaDestino]) / taxasCambio[moedaOriginal]
                        print(f"\nValor Convertido: {valorConvertido} {moedaDestino}")
                    else:
                        print("Moeda não reconhecida")
                else:
                    print("Moeda não reconhecida")


            elif (opcaoCliente == 3):
                print()

            else:
                print("********** OPÇÃO INVÁLIDA **********")


    elif (opcaoLogin == 0):  # SAIR
        print("********** SAIR **********")
        print("Obrigado. Até à próxima!")


    else:
        print("********** OPÇÃO INVÁLIDA **********")
