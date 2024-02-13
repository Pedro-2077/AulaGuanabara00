n = 0
opcao = ''
maior = 0
menor = 0
media = 0
soma =0
cont = 0

while opcao != 'n':
    n = int(input('Digite um valor:'))
    soma = soma + n
    cont += 1
    if menor == 0:
        menor = n
    elif n < menor:
        menor = n
    elif n > maior:
        maior = n
    opcao = input('Deseja continuar? [s/n]:').lower()

media = soma / cont

print('Quantidade de valores digitados:{}'.format(cont))
print('A soma dos valores foi {}'.format(soma))
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))
print('A media foi {}'.format(media))