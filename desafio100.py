print('===== DESAFIO 100 =====')

from random import randint

def sorteia(lista):
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
    print(f'Os valores sorteados foram: {lista}')
    somapar(lis)


def somapar(lista):
    soma = 0
    for par in range(0, len(lista)):
        if lista[par] % 2 == 0:
            soma += lista[par]
    print(f'A soma é: {soma}')




lis = list()
sorteia(lis)




