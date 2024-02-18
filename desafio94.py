print('===== DESAFIO 94 =====')

dados = {}
pessoas = []
soma = 0
mulheres = list()

while True:
    dados['nome'] = str(input('Digite seu nome:')).strip().upper()
    dados['sexo'] = str(input('Sexo [M/F]:')).strip().upper()[0]

    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Sexo [M/F]:')).strip().upper()[0]

    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])

    dados['idade'] = int(input('Digite sua idade: '))
    soma = dados['idade'] + soma
    print(soma)

    op = str(input('Deseja continuar [S/N]:')).strip().upper()[0]

    pessoas.append(dados.copy())

    if op in 'N':
        break

    while op not in 'SN':
        op = str(input('Deseja continuar [S/N]:')).strip().upper()[0]

    print('-='*30)

media = soma / len(pessoas)
print('-='*30)

print(f'A)Ao todo temos {len(pessoas)} pessoas cadastrada')
print(f'B) A média de idade é de {media}')
print(f'C) As mulheres foram cadastradas: {mulheres} ')
print(f'D)A lista de pessoas que estão acima da media:')
for p in pessoas:
    for k, v in p.items():
        if p['idade'] > media:
            print(f'{k} = {v};', end=' ')




