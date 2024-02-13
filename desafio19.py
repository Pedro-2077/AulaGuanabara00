import random

print('====== DESAFIO19 ======')

nome1 = input('Digite o nome do primeiro:')
nome2 = input('Digite o nome do segundo:')
nome3 = input('Digite o nome do terceiro:')
nome4 = input('Digite o nome do quarto:')

lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)

print('O nome sorteado é {}'.format(escolhido))
