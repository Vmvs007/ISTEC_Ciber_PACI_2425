valor = int(input("Insira o valor €: "))

if(valor%5==0):
    notas = valor // 200
    print("Notas de 200€:", notas)

    valor = valor % 200

    notas = valor // 100
    print("Notas de 100€:", notas)

    valor = valor % 100

    notas = valor // 50
    print("Notas de 50€:", notas)

    valor = valor % 50
    
    notas = valor // 20
    print("Notas de 20€:", notas)

    valor = valor % 20

    notas = valor // 10
    print("Notas de 10€:", notas)

    valor = valor % 10

    notas = valor // 5
    print("Notas de 5€:", notas)

else:
    print("Não damos trocos")