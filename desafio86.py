print('===== DESAFIO 86 =====')

matriz = list()
dados = list()

for d in range(0, 3):
    for c in range(0, 3):
        dados.append(int(input(f'Digite um valor para [{d}, {c}]:')))

    matriz.append(dados[:])
    dados.clear()

print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:}]',end='')
        if c == 2:
            print('\t')

