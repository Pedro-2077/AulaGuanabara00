print('===== DESAFIO 53 =====')

nome = str(input('Digite uma palavra:')).strip().upper()
palavras = nome.split()
junto = ''.join(palavras)
inverso = ''


for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
    #O inverso esta concatenado com cada posição do junto que esta decrecendo / para entender melhor desative o comentario abaixo
    #print(inverso)
if inverso == junto:
    print('Palindromo')
else:
    print('Não é palindormo')