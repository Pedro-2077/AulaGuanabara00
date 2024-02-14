print('===== DESAFIO 77 =====')

palavra = (str(input('Digite uma palavra: ')),str(input('Digite uma palavra: ')),
           str(input('Digite uma palavra: ')), str(input('Digite uma palavra: ')))

'''for letra in range(0, len(palavra)):
    print(f'\n{palavra[letra]} = ', end='')
    for letra2 in range(0, len(palavra[letra])):
        if palavra [letra][letra2] in 'aAeEeIiOoUuUu':
            print(f'{palavra[letra][letra2]}', end=' ')
'''
#MODO GUANABARA

for letra in palavra:
    print(f'\nA palavra {letra}:',   end=' ')
    for letra2 in letra:
        if letra2.lower() in 'aeiou':
            print(f'{letra2}', end=' ')
