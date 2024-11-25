nota1 = float(input("Insira a nota1: "))
nota2 = float(input("Insira a nota2: "))
nota3 = float(input("Insira a nota3: "))

mediaPonderada = nota1 * 0.25 + nota2 * 0.35 + nota3 * 0.4

# print("Média Ponderada:",mediaPonderada)

if(mediaPonderada>=9.5):
    print("Está aprovado")
else:
    print("Está reprovado")