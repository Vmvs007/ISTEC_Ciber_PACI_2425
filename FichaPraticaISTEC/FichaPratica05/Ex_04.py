# Criar a lista
lista = []

# Preencher a lista
for i in range(0, 10):
    num = int(input(f"Insira na lista[{i}]: "))
    lista.append(num)

lista.sort()
menor = lista[0]

print("Maior:",menor)
