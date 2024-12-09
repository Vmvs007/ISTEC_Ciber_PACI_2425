alunos = {
    'Vitor': [20, 15, 13],
    'Joao': [10, 6, 7],
    'Maria': [12, 13, 14],
    'Joaquim': [13, 14, 20],
    'Joana': [2, 18, 5]
}

nome = input("Aluno a pesquisar: ")

if nome in alunos:
    notas = alunos[nome]
    somaNotas = 0

    for i in range(0, len(notas)):
        somaNotas += notas[i]

    media = somaNotas / len(notas)
    print(f"Média {nome}: {media}")

else:
    print("Aluno não existe")