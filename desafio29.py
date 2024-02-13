print('====== DESAFIO 29 ====')

km = float(input('Digite a velocidade que esta:'))

if km > 80:
    km = km - 80
    km = km * 7
    print('Você tera que pagar R${}'.format(km))
else:
    print('Passou, parabens')