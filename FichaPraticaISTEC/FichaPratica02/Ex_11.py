saldo = float(input("Insira o saldo: "))
movimento = float(input("Insira o valor a movimentar: "))

if (saldo + movimento >= 0):
    saldo = saldo + movimento
else:
    print("Operação inválida")


print("Saldo Atual:", saldo)
