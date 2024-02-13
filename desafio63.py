print('====== DESAFIO 63 ====')

soma = 0
cont = 0
n = 0

while n != 999:
    n = int(input('Digite o numero [999 para parar]: '))

    if n != 999:
        soma += n
        cont += 1

print('A soma dos numeros digitados foi {} \nE a quantidade de vezes foi {}'.format(soma,cont))