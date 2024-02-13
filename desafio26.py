print('===== DESAFIO 26 =====')

frase = str(input('Digite uma frase qualquer:'))

frase = frase.strip().lower()
print('A letra A aparece {} na frase'.format(frase.count('a')))
print('A primeira vez que aparece o A é:{}'.format(frase.find('a')))
print('A ultima vez que aparece é:{}'.format(frase.rfind('a')))
