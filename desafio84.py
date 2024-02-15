print('===== DESAFIO 84 =====')

pessoas = list()
dado = list()
maior = list()
menor = list()

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()

    op = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while op not in 'SN':
        print('ERRO! Responda')
        op = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if op in 'N':
        break

for p in pessoas:
    if p[1] >= 100:
        maior.append(p[:])
    elif p[1] <= 70:
        menor.append(p[:])
print('-='*30)

print(f'Foram cadastradas {len(pessoas)}')
print(f'O maior peso foi {maior}')
print(f'O menor peso foi {menor}')
