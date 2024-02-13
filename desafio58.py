import random
from random import randint
print('====== DESAFIO 58 ====')

num = int(input('Digite um numero entre 0 e 10: '))
maquina = random.randint(0, 10)

while maquina != num:
    num = int(input('Digite um numero novamente VOCE ERROU:'))