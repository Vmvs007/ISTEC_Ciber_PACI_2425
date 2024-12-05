# Criar a lista
lista = []

# Preencher a lista
for i in range(0, 10):
    num = int(input(f"Insira na lista[{i}]: "))
    lista.append(num)

print("_____________________________________")

# Imprimir por ordem
for i in range(0, 10):
    print(f"lista[{i}]: {lista[i]}")

print("_____________________________________")

# Imprimir por ordem
print(lista)
