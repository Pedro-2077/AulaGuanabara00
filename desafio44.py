import math
print(' ====== DESAFIO 44 ======')

parcela = 0

preço = float(input('Digite o valor:'))
formarPagamento = str(input('Digite a forma de pagamento:')).lower()

if 'cartão' in formarPagamento:
    parcela = int(input('Quantas parcelas?'))

else:
    preço = preço * 0.90
    print('Valor:{}'.format(preço))

if parcela == 1:
    preço = preço * 0.95
    print('Valor:{}'.format(preço))
elif parcela == 2:
    print('Valor:{}'.format(preço))
elif parcela >= 3:
    preço = preço * 1.20
    print('Valor:{}'.format(preço))

