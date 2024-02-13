print('====== DESAFIO 33 ====')

num = int(input('Digite um numero:'))
num2 = int(input('Digite outro numero:'))
num3 = int(input('Digite mais um numero:'))
maior = 0
menor = 0
if num > num2 and num > num3:
    maior = num

    if num2 > num3:
        menor = num3
    else:
        menor = num2

if num2 > num and num2 > num3:
    maior = num2

    if num > num3:
        menor = num3
    else:
        menor = num

if num3 > num and num3 > num2:
    maior = num3

    if num2 > num:
        menor = num
    else:
        menor = num2

print('O maior é:{}'.format(maior))
print('O menor numero é:{}'.format(menor))

