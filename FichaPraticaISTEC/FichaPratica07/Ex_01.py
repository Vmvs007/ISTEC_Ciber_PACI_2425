
ranking = {
    "Vitor": 12,
    "Carlos": 8,
    "Ana": 10,
    "David": 10,
    "Eva": 7
}

names = list(ranking.keys())
rankings = list(ranking.values())

for i in range(len(rankings)):
    for j in range(0, len(rankings) - i - 1):
        if rankings[j] < rankings[j + 1]:
            rankings[j], rankings[j + 1] = rankings[j + 1], rankings[j]
            names[j], names[j + 1] = names[j + 1], names[j]

for i in range(len(names)):
    print(f"{names[i]}: {rankings[i]}")
