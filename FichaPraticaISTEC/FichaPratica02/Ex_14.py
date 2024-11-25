a = int(input("Insira um número: "))
b = int(input("Insira um número: "))
c = int(input("Insira um número: "))

if (a < b and a < c):  # a ... ...
    if (b < c):
        print(a, b, c)
    else:
        print(a, c, b)

if (b < a and b < c):  # b ... ...
    if (a < c):
        print(b, a, c)
    else:
        print(b, c, a)

if (c < a and c < b):  # c ... ...
    if (a < b):
        print(c, a, b)
    else:
        print(c, b, a)

