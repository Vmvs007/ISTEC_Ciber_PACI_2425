i = int(input("Insira um ínicio: "))
limite = int(input("Insira um limite: "))
salto = 1

while (i <= limite):
    if (i % 5 == 0):
        print(i)

    i += salto
