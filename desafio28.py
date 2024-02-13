from random import randint

numero = randint(0,5)

numeroTentativa = int(input('Acerte o numero entre 0 e 5:'))

if numeroTentativa == numero:
    print('Você é um cagão!Acertou miseravel.')
else:
    print('Você errou, sua mãe te macumbou')