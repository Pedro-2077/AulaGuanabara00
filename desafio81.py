print('===== DESAFIO 81 =====')

lista = list()
cont = 0

while True:
    lista.append(int(input('Digite um valor:')))
    cont += 1
    op = str(input('DESEJA continuar? [S/N] ')).strip().upper()[0]

    while op not in 'SN':
        op = str(input('DESEJA continuar? [S/N] ')).strip().upper()[0]
    if op in 'N':
        break

print('A lista', lista)
print(f'Foram digitados {cont}')
lista.reverse()
print(f'Os valores digitados na ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 esta lista')
else:
    print('O valor 5 nao esta lista')