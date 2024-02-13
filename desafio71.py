print('===== DESAFIO 71 =====')

valor = int(input('Digite o valor a sacar:'))
soma = 0
cont50 = cont20 = cont10 = cont1 = 0

while True:

    if (soma + 50) <= valor:
        cont50 += 1
        soma += 50
    elif (soma + 20) <= valor:
        cont20 += 1
        soma += 20
    elif (soma + 10) <= valor:
        cont10 += 1
        soma += 10
    elif (soma + 1) <= valor:
        cont1 += 1
        soma += 1

    elif soma == valor:
        break

print(f'Total de {cont50} R$50')
print(f'Total de {cont20} R$20')
print(f'Total de {cont10} R$10')
print(f'Total de {cont1} R$1')


