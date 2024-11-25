salario=float(input("Insira o salário: "))

if(salario<=15000):
    imposto = salario*0.2
    print("Imposto 20%:", imposto)
else:
    imposto = salario*0.3
    print("Imposto 30%:", imposto)


