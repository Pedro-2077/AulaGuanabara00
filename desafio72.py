print('===== DESAFIO 72 =====')

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um numero entre 0 e 20:'))
    if 0 <= n <= 20:
        break

print(f'Voce digitou o numero {numeros[n]}')
