print('===== DESAFIO 31 =====')

numero = int(input('Digite a viagem em KM:'))

if numero <=200:
    numero = numero * 0.50
else:
    numero = numero * 0.45
print('O valor é:{}'.format(numero))