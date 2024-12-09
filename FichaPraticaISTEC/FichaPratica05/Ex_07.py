from FichaPratica05.Ex_03 import maior

lista = []

# Preencher a lista
for i in range(0, 10):
    num = int(input(f"Insira na lista[{i}]: "))
    lista.append(num)

maiorPar = -1

print("_____________________________________")

for i in range(0, 10):
    if (lista[i] % 2 == 0):

        if (maiorPar % 2 != 0):
            maiorPar = lista[i]

        if (lista[i] > maiorPar):
            maiorPar = lista[i]


if (maiorPar % 2 == 0):
    print("Maior Par: ", maiorPar)
else:
    print("Não há pares")
