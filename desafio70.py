print('===== DESAFIO 70 =====')
soma = 0
maisMil = 0
nomeProduto = ''
menorValor = 0
while True:
    nomeP =str(input('Diga o nome do produto: ')).strip().lower()
    preco =float(input('Digite o preço do produto: R$'))
    soma += preco

    if preco > 1000:
        maisMil += 1

    if menorValor == 0:
        menorValor = preco
        nomeProduto = nomeP
    if preco < menorValor:
        menorValor = preco
        nomeProduto = nomeP

    op = str(input('Deseja continuar: [S/N] ')).strip().lower()

    while op not in 'sn':
        op = str(input('Deseja continuar: [S/N]')).strip().lower()

    if op in 'n':
        break

print(f'O total gasto na compra R${soma:.2f}')
print(f'Temos {maisMil} mais de R$1000.00')
print(f'O produto mais barato é {nomeProduto} que custa R${menorValor}')
