print('===== DESAFIO 76 =====')
lista = ()
while True:
    produto = str(input('Digite o nome do produto:'))
    preco = float(input('Digite o valor do produto:'))

    listaA = (produto, preco)
    lista += listaA
    op = str(input('Deseja Sair do Programa? [S/N] ')).strip().upper()

    if op in 'sS':
        break

print('-'*40)
print(' '*8,'LISTAGEM DE PREÇOS')
print('-'*40)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R$ {lista[c]:>6.2f}')

print('-'*40)