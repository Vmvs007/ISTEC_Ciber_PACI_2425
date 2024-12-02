numero = int(input("Insira um número: "))

anterior = numero - 5
sucessor = numero + 5

while (anterior <= sucessor):
    if (anterior != numero):
        print(anterior)
    anterior += 1
