from random import randint

print('===== DESAFIO 68 =====')
cont = 0

while True:
    jogador = int(input('Digite um numero inteiro:'))
    opcao = str(input('Par ou Impar?:')).strip().upper()
    computador = randint(1, 10)
    soma = jogador + computador

    if soma % 2 == 0:
        if opcao == 'PAR':
            print(f'A soma dos valores {jogador} e {computador} = {soma}/PAR')
            print(f'O jogador ganhou')
            cont += 1
        else:
            print(f'A soma dos valores {jogador} e {computador} = {soma}/PAR')
            print(f'O Computador ganhou')
            break
    elif soma % 2 == 1:
            if opcao == 'IMPAR':
                print(f'A soma dos valores {jogador} e {computador} = {soma}/IMPAR')
                print(f'O jogador ganhou')
            else:
                print(f'A soma dos valores {jogador} e {computador} = {soma}/IMAPAR')
                print(f'O Computador ganhou')
                break

print(f'Voce ganhou {cont} vezes no GAME')

