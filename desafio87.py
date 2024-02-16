print('===== DESAFIO 87 =====')

matriz = list()
dados = list()
soma = 0
soma3 = 0
for c in range(0, 3):
    for d in range(0, 3):
        dados.append(int(input(f'Digite o valor [{c}, {d}]:')))
        if dados[d] % 2 == 0:
            soma += dados[d]
        if d == 2:
            soma3 += dados[d]
    matriz.append(dados[:])
    dados.clear()

for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]}]', end='')
    print('\t')

print(f'A soma de todos os numeros é {soma}')
print(f'A soma da 3 coluna {soma3}')
print(f'O maior valor da segunda linha é:{max(matriz[1])}')
