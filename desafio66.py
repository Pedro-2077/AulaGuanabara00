print('===== DESAFIO 66 =====')

s = c = 0

while True:
    n = int(input('Digite um numero:'))
    if n == 999:
        break
    s += n
    c +=1

print(f'A quantidade de numeros é {c} e a soma valores é {s}')
