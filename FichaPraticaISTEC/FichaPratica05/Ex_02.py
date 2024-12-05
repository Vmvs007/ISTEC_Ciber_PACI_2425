listaComissoes = []
somatorio = 0

for i in range(0, 12):
    listaComissoes.append(int(input(f"Insira comissões do mês {i+1}: ")))

    somatorio += listaComissoes[i]

print("Soma de Comissões:", somatorio)
