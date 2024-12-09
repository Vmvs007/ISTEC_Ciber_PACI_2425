# Criar a lista
lista = []

# Preencher a lista
for i in range(0, 10):
    num = int(input(f"Insira na lista[{i}]: "))
    lista.append(num)

maior = lista[0]

for i in range(0, 10):
    if (lista[i] > maior):
        maior = lista[i]

print("Maior:", maior)
