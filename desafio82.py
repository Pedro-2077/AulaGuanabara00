print('====== DESAFIO82 ======')
numeros = list()
numerosPares = list()
numerosImpares = list()
copia = 0
while True:
    copia = int(input('Digite um numero:'))

    if copia % 2 == 0:
        numerosPares.append(copia)
    elif copia % 2 == 1:
        numerosImpares.append(copia)

    numeros.append(copia)

    resp = str(input('Deseja continuar S/N?:')).strip().upper()[0]
    if resp == 'N':
        break
    while resp not in 'SN':
        print('ERRO!')
        resp = str(input('Deseja continuar S/N?:')).strip().upper()[0]


print(f'A lista completa é {numeros}')
print(f'A lista dos numeros pares {numerosPares}')
print(f'A lista dos numeros impares {numerosImpares}')

