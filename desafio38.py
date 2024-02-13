print('===== DESAFIO 38 =====')

numero = int(input('Digite um numero:'))
numero2 = int(input('Digite outro numero:'))

if numero > numero2:
    print('O numero {} é maior que {}'.format(numero, numero2))
elif numero2 > numero:
    print('O numero {} é maio que {}'.format(numero2, numero))
else:
    print('Os numeros são iguais')