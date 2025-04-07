def ler_inteiro_positivo():
    numero = -1

    while (numero < 0):
        numero = int(input("Insira um número (inteiro e positivo): "))

    return numero


def imprimir_asteriscos(vezes):
    for i in range(vezes):
        print("*", end="")
