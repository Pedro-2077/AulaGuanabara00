from datetime import date

print('====== DESAFIO 39 ====')

atual = date.today().year
data = int(input('Digite o ano de nascimento: '))
idade = atual  - data

if idade < 18:
    falta = 18 - idade
    print('Ainda vai se alistar, falta {} anos'.format(falta))
elif idade > 18:
    falta = idade - 18
    print('Sua idade ja passou do alistamento a {} anos'.format(falta))
elif idade == 18:
    print('Esta na hora de se alistar')