print('===== DESAFIO 83 =====')

expresao = str(input('Digite uma frase:'))
cont = 0
cont2 = 0

for letra in range(0, len(expresao)):
    if expresao[letra] in '(':
        cont = expresao.count('(')
        print('entrei')
    elif expresao[letra] in ')':
        print('entrei 2')
        cont2 = expresao.count(')')
if cont2 == cont:
    print('Pode ser uma expresão')
else:
    print('Não pode ser um expresão')