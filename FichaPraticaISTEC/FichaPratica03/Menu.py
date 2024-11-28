
opcao = 1

while(opcao!=0):
    print("\n\n**** Menu do Meu Programa ****")
    print("1. Números de 1 a 250")
    print("2. Números pares de 2 a 400")
    print("3. abc")
    print("4. 123")
    print("0. Sair")

    opcao= int(input("Selecione a sua opção: "))

    match opcao:
        case 1: # Números de 1 a 250
            numero = 1

            while (numero <= 250):
                print(numero)
                numero = numero + 1


        case 2: # Números pares de 2 a 400
            numero = 2

            while (numero <= 400):
                print(numero)
                numero += 2  # numero = numero + 2

        case 3: # abc
            print("abc")

        case 4: # 123
            print("123")

        case 0: # Sair
            print("Obrigado. Volte sempre :D")

        case _: print("Opção Inválida")

    print("_______________________________________________")