horas = int(input("Insira as horas: "))
minutos = int(input("Insira os minutos: "))

if (horas <= 12):
    # Manhã - AM
    print(f"{horas}:{minutos} AM")
else:
    # Tarde - PM
    horas = horas - 12
    print(f"{horas}:{minutos} PM")