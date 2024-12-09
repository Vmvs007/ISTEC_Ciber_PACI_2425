# Criar a lista
lista = []

# Preencher a lista
for i in range(0, 10):
    num = int(input(f"Insira na lista[{i}]: "))
    lista.append(num)

lista.sort()
maior = lista[9]

print("Maior:",maior)
