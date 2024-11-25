num1=int(input("Insira um número: "))
num2=int(input("Insira um número: "))
num3=int(input("Insira um número: "))

if(num1<num2 and num1<num3):
    print("Menor:",num1)
elif (num2<num3):
    print("Menor:",num2)
else:
    print("Menor:",num3)

