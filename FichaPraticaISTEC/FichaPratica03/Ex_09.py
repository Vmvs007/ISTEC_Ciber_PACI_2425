numero = 0
contador = -1
somatorio = 1

while (numero != -1):
    numero = int(input("Insira um número: "))

    contador += 1
    somatorio += numero

    # print("Somatório:", somatorio)
    # print("Contador:", contador)

media = somatorio / contador
print("Média:", media)
