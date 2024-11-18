preco1 = float(input("Insira o preço do produto1: "))
preco2 = float(input("Insira o preço do produto2: "))
preco3 = float(input("Insira o preço do produto3: "))

total = preco1+preco2+preco3
totalComDesconto = total*0.9

print("Preço Total:",total)
print("Preço com 10% de Desconto:",totalComDesconto)