print('===== DESAFIO22 =====')

nome = str(input('Digite seu nome completo:'))
nomeLower = nome.lower()
nomeUpper = nome.upper()
nomeNew = nome.replace(' ', '')
nomePrime = nome.split()
nomePrimeQtd = len(nomePrime[0])

print('Seu nome:{}'.format(nome))
print('Seu nome minusculo:{}'.format(nomeLower))
print('Seu nome maiusculo:{}'.format(nomeUpper))
print('Seu nome tamanho:{}'.format(len(nomeNew)))
print('Seu primeiro nome tamanho:{}'.format(nomePrimeQtd))