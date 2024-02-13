print('====== DESAFIO 52 ====')

numero = int(input('Digite um numero:'))
cont = 0
for c in range(numero,0,-1):
    if numero % c == 0:
        cont += 1
if cont == 2:
    print('O numero {} é primo'.format(numero))
else:
    print('O numero {} não é primo'.format(numero))