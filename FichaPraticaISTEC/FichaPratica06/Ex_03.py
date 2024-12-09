tradutor={
    'dog':'cão',
    'cat':'gato',
    'house':'casa',
    'car':'carro',
    'computer':'computador'
}

palavra = input("Insira a palavra em inglês para traduzir: ")

if palavra not in tradutor:
    print("Não temos tradução")
else:
    print(tradutor[palavra])

