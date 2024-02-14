print('===== DESAFIO 75 =====')
numerosPares = 0
'''numeros = [0, 0, 0, 0]

for c in range(0, 4):
    numeros[c] = int(input('Digite um numero'))
    if numeros[c] % 2 == 0:
        numerosPares += 1


print(f'Os valores digitados são {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O valor 3 apareceu {numeros.index(3)+1}')

print(f'Valores Pares são {numerosPares}')

'''
'''
n = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
n4 = int(input('Digite um numero: '))

lista = (n, n2, n3, n4)
print(lista)

print(f'\n\nO numeros {lista}')
print(f'O numero 9 apareceu {lista.count(9)}vez')
if 3 in lista:
    print(f'O numero 3 apareceu {lista.index(3)+1} na posição')
else:
    print('O numero 3 aparece na lista 0 vezes')

for c in lista:
    if c % 2 == 0:
        numerosPares += 1

print(f'Os valores pares digitados são {numerosPares}')
'''
#METODO QUANABA

n = ((int(input('Digite um numero:'))), (int(input('Digite um numero:'))), (int(input('Digite um numero:'))),
     (int(input('Digite um numero:'))), (int(input('Digite um numero:'))))

print(f'Os valores digitados são: {n}')


