#PRATICA

'''for c in range(0, 11):
    print(c)'''

#WHILE
c = 0
'''
 while c < 10:
    print(c)
    c += 1

valor = 1
while valor != 0:
    valor = int(input('Digite un numero:'))
print('Saiu')

resposta = input('s/n').upper()

while resposta == 'S':
    resposta = input('Deseja Continuar?').upper()
print('Finalizado')

'''

n = 1
pares = 0
inpares = 0

while n != 0:
    n = int(input('Digite um numero:'))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            inpares += 1


print(pares,inpares)
