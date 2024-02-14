from random import randint
print('===== DESAFIO 74 =====')
menor = maior = 0

n = (randint(1, 10), randint(1, 10), randint(1,10), randint(1,10), randint(1, 10))

for c in range(0, len(n)):
    if menor == 0:
        menor = n[c]
    elif n[c] < menor:
        menor = n[c]

    if n[c] > maior:
        maior = n[c]

print(f'Os valores sorteados {n}')
print(f'O maior valor é {maior} e o menor é {menor}')

#OUTRA MANEIRA DE VER O MENOR VALOR

print(f'O maior valor é {max(n)}') #max MAIOR DA TUPLA
print(f'O menor valor é {min(n)}')#menor da TUPLA
