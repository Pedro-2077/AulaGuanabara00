print('====== DESAFIO32 ======')

num = int(input('Digite um numero:'))

if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print('O ano {} é bissexto'.format(num))
else:
    print('O ano não é bissexto')