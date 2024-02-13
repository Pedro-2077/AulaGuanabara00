import random
import math

print('====== DESAFIO 20 ======')

nome = input('Digite o primeiro nome:')
nome2 = input('Digite o segundo:')
nome3 = input('Digite o terceiro:')
nome4 = input('Digite o Quarto:')
lista = [nome, nome2, nome3, nome4]
random.shuffle(lista)

print('A ordem vai ser {}'.format(lista))

