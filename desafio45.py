import random
from time import sleep
print('====== DESAFIO 45 ====')

jogadorMaquina = ['pedra', 'papel', 'tesoura']
jogadorMaquina = random.choice(jogadorMaquina)

nome = input('Qual é o seu nome:')
escolha = input('Escolha:pedra, papel ou tesoura:').lower()

print('JOOOOO')
sleep(1)#IMPORTADO DA BIBLIOTECA TIME deixa 1 segundo de delay em cada print
print('KENNNN')
sleep(1)
print('POOOO')
sleep(1)

if escolha == 'pedra' and jogadorMaquina == 'tesoura':
    print('{}:{} e Maquina:{} / Vencedor {}'.format(nome, escolha, jogadorMaquina, nome))
elif escolha == 'pedra' and jogadorMaquina == 'papel':
    print('{}:{} e Maquina:{} / Vencedor {}'.format(nome, escolha, jogadorMaquina, 'jogadorMaquina'))
elif escolha == 'papel' and jogadorMaquina == 'pedra':
    print('{}:{} e Maquina:{} / Vencedor {}'.format(nome, escolha, jogadorMaquina, nome))
elif escolha == 'papel' and jogadorMaquina == 'tesoura':
    print('{}:{} e Maquina:{} / Vencedor {}'.format(nome, escolha, jogadorMaquina, 'jogadorMaquina'))
elif escolha == 'tesoura' and jogadorMaquina == 'pedra':
    print('{}:{} e Maquina:{} / Vencedor {}'.format(nome, escolha, jogadorMaquina, 'jogadorMaquina'))
elif escolha == 'tesoura' and jogadorMaquina == 'papel':
    print('{}:{} e Maquina:{} / Vencedor {}'.format(nome, escolha, jogadorMaquina, nome))
else:
    print('{}:{} e Maquina:{} / Empate'.format(nome, escolha, jogadorMaquina))






