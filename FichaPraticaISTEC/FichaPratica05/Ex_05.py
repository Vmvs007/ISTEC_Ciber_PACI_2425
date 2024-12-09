lista = []

num = 0
somatorio = 0

while (num >= 0):
    num = int(input("Insira um número na lista: "))
    lista.append(num)

lista.pop(len(lista) - 1)

for i in range(0, len(lista)):
    somatorio+=lista[i]

media = somatorio / len(lista)

print("Média", media)
