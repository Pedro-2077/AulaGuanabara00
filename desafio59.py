from time import sleep
print('====== DESAFIO 59 ====')

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
opcao = 0

sleep(1)

while opcao != 5:
    print('''\033[35;40mEscolha:\033[m
    [1]Soma
    [2]Multiplicar
    [3]Maior
    [4]Novos Numeros
    [5]Sair do Programa''')
    opcao = int(input('Escolha sua opção:'))

    if opcao == 1:
        soma = n1 + n2
        print('A soma dos numeros {} + {} = {}'.format(n1, n2, soma))
    if opcao == 2:
        multiplicar = n1 * n2
        print('O produto dos numeos {} * {} = {}'.format(n1, n2, multiplicar))
    if opcao == 3:
        if n1 > n2:
            print('O maior numero entre {} e {} é: {}'.format(n1, n2, n1))
        else:
            print('O maior numero entre {} e {} é: {}'.format(n2, n1, n2))
    if opcao == 4:
        n1 = int(input('Digite um novo numero:'))
        n2 = int(input('Digite outro numero:'))
