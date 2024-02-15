print('===== DESAFIO 79 =====')

lista = list()
while True:
    copia = int(input('Digite um valor: '))
    if copia not in lista:
        lista.append(copia)
        print('Valor adicionado')
    else:
        print('Valor Ja existe na lista NÂO Adicionado')
    op = str(input('Quer continuar? [S/N] ')).upper().strip()
    if op in 'Nn':
        break

print(sorted(lista))
