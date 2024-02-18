print('===== DESAFIO 93 =====')

jogador = {}
dadoGol = list()
soma = 0

jogador['nome'] = str(input('Nome do Jogado:'))
n = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

for c in range(0, n):
    dadoGol.append(int(input(f'Quantos gols na partida {n}?:')))
    soma = soma + dadoGol[c]

jogador['Gosl'] = dadoGol
jogador['total'] = soma

print('=-'*30)
print(jogador)
print('=-'*30)

print(f'O campo nome tem o valor {jogador['nome']}')
print(f'O campo gols tem o valor {dadoGol}')
print(f'O campo total de {jogador['total']} gols')

print('=-'*30)
print(f'O jogador {jogador['nome']} jogou {n}:')
for pos, itens in enumerate(dadoGol):
    print(f'Na partida {pos}, fez {itens} gols')
print('=-'*30)
print(f'Foi um total de {jogador["total"]} gols')

