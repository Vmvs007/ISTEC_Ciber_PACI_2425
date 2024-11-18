totalSegundosAlbum = 0

minutosMusica = int(input("Minutos Música 1: "))
segundosMusica = int(input("Segundos Música 1: "))

totalSegundosAlbum= totalSegundosAlbum +(minutosMusica*60)+segundosMusica

minutosMusica = int(input("Minutos Música 2: "))
segundosMusica = int(input("Segundos Música 2: "))

totalSegundosAlbum= totalSegundosAlbum +(minutosMusica*60)+segundosMusica

minutosMusica = int(input("Minutos Música 3: "))
segundosMusica = int(input("Segundos Música 3: "))

totalSegundosAlbum= totalSegundosAlbum +(minutosMusica*60)+segundosMusica

minutosMusica = int(input("Minutos Música 4: "))
segundosMusica = int(input("Segundos Música 4: "))

totalSegundosAlbum= totalSegundosAlbum +(minutosMusica*60)+segundosMusica

minutosMusica = int(input("Minutos Música 5: "))
segundosMusica = int(input("Segundos Música 5: "))

totalSegundosAlbum= totalSegundosAlbum +(minutosMusica*60)+segundosMusica

print("Total de Segundos do Album:",totalSegundosAlbum)

horas = totalSegundosAlbum // 3600
minutos = (totalSegundosAlbum// 60) - (horas*60)
segundos = totalSegundosAlbum - (horas*3600) - (minutos*60)

print("Total do Álbum")
print(f"{horas}h {minutos}m {segundos}s")