from math import factorial
print('===== DESAFIO 60 =====')

fatorial = int(input('Digite o valor um numero para calcular seu fatorial: '))
soma = 1
print('Calculando{}!:{}'.format(fatorial,fatorial), end='')

while fatorial > 0:

    soma *= fatorial
    print(' x {}'.format(fatorial), end='')
    fatorial -= 1

print(' = {}'.format(soma))

'''OUTRA FORMA DE FAZER IMPORTANDO A BIBLIOTECA MATH'''

inteiro = int(input('Digite um numero:'))
f = factorial(inteiro)
print(f)
