salario = float(input("Insira o salário: "))

if (salario <= 15000):
    imposto = salario * 0.2
    print("Imposto 20%:", imposto)

elif (salario <= 20000):
    imposto = salario * 0.3
    print("Imposto 30%:", imposto)

elif (salario <= 25000):
    imposto = salario * 0.35
    print("Imposto 35%:", imposto)

else:
    imposto = salario * 0.4
    print("Imposto 40%:", imposto)


