print('===== DESAFIO 34 =====')
salario = float(input('Digite seu salario:'))

if salario > 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15

print('Seu novo salario:{:.2f}'.format(aumento))