print('===== DESAFIO 35 =====')

a = float(input('Digite um segmento:'))
b = float(input('Digite outro segmento:'))
c = float(input('Digite o terceiro segmento:'))

if (a + b) > c and (b + c) > a and (c + a) > b:
    print('O segmentos podem formar um triangulo')
else:
    print('Os segmentos não podem ser um triangulo')