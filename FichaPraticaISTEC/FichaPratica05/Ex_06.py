# Criar a lista

lista = []

crescente = True

# Preencher a lista
for i in range(0, 10):
    num = int(input(f"Insira na lista[{i}]: "))
    lista.append(num)

print("_____________________________________")

for i in range(1, 10):
    if (lista[i] <= lista[i - 1]):
        crescente = False

if (crescente):
    print("Crescente")
else:
    print("Não crescente")
