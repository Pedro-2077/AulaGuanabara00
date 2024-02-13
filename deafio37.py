print( '===== DESAFIO 37 =====')

num = int (input('Digite um numero:'))

print('''Escolha as as formas de conversãos
[01] Binario
[02] Octal
[03] Hexadecimal''')

opcao = int(input('Digite a opção:'))

if opcao == 1:
    print('O valor {} covertido para Binario {}'.format(num, bin(num)[2:]))

elif opcao == 2:
    print('O valor {} convertido para Octal {}'.format(num, oct(num)[2:]))
else:
    print('O valor {} convertido para Hexadecimal {}'.format(num, hex(num)[2:]))