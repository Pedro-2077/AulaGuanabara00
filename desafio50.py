print('====== DESAFIO 50 ====')
s = 0

for c in range(0, 6):
    n = int(input('Digite um numero:'))
    if n % 2 == 0:
        s = s + n

print('A soma é {}'.format(s))