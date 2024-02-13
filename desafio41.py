from datetime import date

print(' ====== DESAFIO 04 ======')

data = int(input('Digite a sua idade:'))

idade = date.today().year - data

if idade <= 9:
    print('Sua idade é {} anos, Atleta mirim'.format(idade))
elif 9 < idade <= 14:
    print('Sua idade é {} anos, Atleta infantil'.format(idade))
elif 14 < idade <= 19:
    print('Sua idade é {} anos, Atleta junior'.format(idade))
elif idade == 20:
    print('Sua idade é {} anos, Atleta Sênior'.format(idade))
else:
    print('Sua idade é {} anos, Atleta Master'.format(idade))


