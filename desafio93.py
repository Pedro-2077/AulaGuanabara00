print('===== DESAFIO 93 =====')

jogador = {}
dadoGol = list()
soma = 0

jogador['nome'] = str(input('Nome do Jogado:'))
n = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

for c in range(0, n):
    dadoGol.append(int(input(f'Quantos gols na partida {c}?:')))
    soma = soma + dadoGol[c]

jogador['Gosl'] = dadoGol[:]
jogador['total'] = soma #JOGADOR['total'] = SUM(DADOSGOL)

print('=-'*30)
print(jogador)
print('=-'*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('=-'*30)
print(f'O jogador {jogador['nome']} jogou {n}:')
for pos, itens in enumerate(dadoGol):
    print(f'Na partida {pos}, fez {itens} gols')
print('=-'*30)
print(f'Foi um total de {jogador["total"]} gols')

