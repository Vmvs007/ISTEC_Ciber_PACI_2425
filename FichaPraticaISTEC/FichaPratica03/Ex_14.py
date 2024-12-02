quant = int(input("Quantos números quer introduzir: "))
i = 1
crescente = True


numeroAnterior = int(input("Insira um número: "))

while (i < quant):
    numeroAtual = int(input("Insira um número: "))

    if(numeroAnterior>=numeroAtual):
        # Sequência deixa de ser crescente
        crescente=False

    numeroAnterior=numeroAtual
    i += 1


if(crescente):
    print("Crescente")
else:
    print("Não Crescente")


