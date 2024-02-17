from random import randint
from time import sleep
from operator import itemgetter

print('===== DESAFIO 91 =====')

jogador = {'jogador1': randint(1, 6),'jogador2': randint(1, 6), 'jogador3': randint(1, 6)
           , 'jogador4': randint(1, 6), 'jogador5': randint(1, 6), 'jogador6': randint(1, 6)}

jogadores_ordenados = sorted(jogador.items(), key=itemgetter(1), reverse=True )#O ITEMGETTER VAI ORDENAR APARTI DOS VALORES 2
print(jogadores_ordenados)

print('Valores sorteados: ')
for k, v in jogador.items():
    print(f'    {k} tirou {v}')
    sleep(1)

print('Ranking dos jogadores')
for i, v in enumerate(jogadores_ordenados):
    print(f'    {i+1}, jogador {v[0]} fez {v[1]}')
    sleep(1)






