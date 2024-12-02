numero = int(input("Insira um número para calcular o fatorial: "))

fatorial = numero

while (numero > 1):
    fatorial = fatorial * (numero - 1)
    numero -= 1

print("Fatorial:", fatorial)
