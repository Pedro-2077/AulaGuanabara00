print('====== DESAFIO62 ====')

termo = int(input('Quantidade de termos:'))
t = 0
t2 = 1

print('{} -> {}'.format(    t, t2), end='')
cont = 3

while cont <= termo:
    t3 = t + t2
    print(' -> {}'.format(t3), end='')
    t = t2
    t2 = t3
    cont += 1