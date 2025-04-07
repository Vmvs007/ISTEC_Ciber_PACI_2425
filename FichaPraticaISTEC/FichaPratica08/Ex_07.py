from FichaPratica08.Ex_06 import *

numero = int(input("Insira um número: "))
opcao = 1

while (opcao != 0):
    print(f"\n\n********** Análise de um Número: {numero} **********")
    print("1. Par ou Impar")
    print("2. Positivo ou Negativo")
    print("3. Primo ou Não Primo")
    print("4. Perfeito ou Não Perfeito")
    print("5. Triangular ou Não Triangular")
    print("6. Trocar de Número")
    print("0. Sair")

    opcao = int(input("Insira a sua opção: "))

    match (opcao):

        case 1:  # Par ou Impar _____________________________
            if (parImpar(numero)):
                print("Par")
            else:
                print("Impar")

        case 2:  # Positivo ou Negativo _____________________
            if (positivoNegativo(numero)):
                print("Positivo")
            else:
                print("Negativo")

        case 3:  # Primo ou Não Primo _______________________
            if (primo(numero)):
                print("Primo")
            else:
                print("Não Primo")

        case 4:  # Perfeito ou Não Perfeito _________________
            if(perfeito(numero)):
                print("Perfeito")
            else:
                print("Não Perfeito")

        case 5:  # Triangular ou Não Triangular _____________
            print()

        case 6:  # Trocar de Número
            numero = int(input("Insira um número: "))

        case 0:
            print("Sair do Programa...")
        case _:
            print("Opção Inválida!")
