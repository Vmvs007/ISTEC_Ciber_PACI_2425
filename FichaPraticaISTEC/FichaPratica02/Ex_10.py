num1 = float(input("Insira um número: "))
num2 = float(input("Insira um número: "))

operacao = input("Insira a operação ( + - * / ): ")

if (operacao == "+"):
    resultado = num1 + num2
    print("Soma:", resultado)

if (operacao == "-"):
    resultado = num1 - num2
    print("Subtração:", resultado)

if (operacao == "*"):
    resultado = num1 * num2
    print("Multiplicação:", resultado)

if (operacao == "/"):
    resultado = num1 / num2
    print("Divisão:", resultado)

if (operacao != "+" and operacao != "-" and operacao != "*" and operacao != "/"):
    print("Operação Desconhecida")
