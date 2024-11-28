
numero = int(input("Insira um número: "))

resultado = 1
contador = numero

while contador > 1:
    temp = 0
    incremento = resultado
    while incremento > 0:
        temp += contador
        incremento -= 1
    resultado = temp
    contador -= 1

print(f"O fatorial de {numero} é: {resultado}")