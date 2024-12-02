numero = 0

cont_00_25 = 0
cont_26_50 = 0
cont_51_75 = 0
cont_76_100 = 0

while (numero >= 0):
    numero = int(input("Insira um número: "))

    if (0 <= numero <= 25):
        cont_00_25 += 1

    elif (26 <= numero <= 50):
        cont_26_50 += 1

    elif (51 <= numero <= 75):
        cont_51_75 += 1

    elif (76 <= numero <= 100):
        cont_76_100 += 1

print(" [00,25]:", cont_00_25)
print(" [26,50]:", cont_26_50)
print(" [51,75]:", cont_51_75)
print("[76,100]:", cont_76_100)
