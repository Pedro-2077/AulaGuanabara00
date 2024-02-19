print('===== DESAFIO 95 =====')

jogador = dict()
galera = list()
dadoGol = list()
partidas = 0


while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input(f'Quantas partidas o jogador {jogador['nome']} jogou?: '))
    for c in range(0, partidas):
        dadoGol.append(int(input(f'Quantos gols na partida {c+1}:')))

    print(dadoGol)
    jogador['gols'] = dadoGol[:]
    jogador['total'] = sum(dadoGol[:])
    dadoGol.clear()
    galera.append(jogador.copy())

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(galera)
print('-='*30)

print('cod nome                  gols                  Total')
print('-'*30)
for pos,c in enumerate(galera):
    print(f'{pos:>3}', end=' ')
    for v in c.values():
        print(f'{str(v):>15}', end=' ')
    print()
print('-='*30)
while True:
    op = int(input('Mostrando dados de qual jogador? (999 para parar):'))
    if op == 999:
        break
    print('--Levantamento do jogador ', end='')
    for v in galera[op]['nome']:
        print(v, end='')
    print(':')
    for pos, c in enumerate(galera[op]['gols']):
        print(f'No jogo {pos} fez {c} gols \t')
    print('-='*30)




