import random
from time import sleep
print('===== DESAFIO 88 =====')

jogos = list()
dado = list()
qtd = 0

qtd = int(input('Quantos jogos deseja:'))

for c in range(0, qtd):
    for d in range(0, 1):
        dado = (random.randint(1, 60), random.randint(1, 60), random.randint(1, 60)
                , random.randint(1, 60), random.randint(1, 60), random.randint(1, 60))
        jogos.append(dado)
    del dado

jogos.sort()
print('=-'*30)
print(f'Matriz do game:{jogos}')
print('=-'*30)

for pos in range(0, qtd):
    print(f'O jogo {pos+1} é = {jogos[pos]} ')
    sleep(1)





'''for pos, cad in enumerate(jogos):
    print(f'Jogo {pos}:{jogos}')'''
