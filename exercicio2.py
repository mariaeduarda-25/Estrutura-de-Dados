def indice_h_linear(citacoes):
    for h in range(len(citacoes)):
        if citacoes[h] < h + 1:
            return h
    return len(citacoes)

citacoes = [10, 8, 5, 4, 3] 
print("Índice-h linear:", indice_h_linear(citacoes))