print('===== DESAFIO 89 =====')

alunos = list()
dados = list()
c = 1
media = 0
while True:
    dados.append(str(input('Nome do aluno: ')))
    dados.append(float(input(f'Nota da AV{c}: ')))
    c += 1
    dados.append(float(input(f'Nota da AV{c}: ')))
    # print(dados)

    alunos.append(dados[:])
    dados.clear()

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N]').strip().upper()[0]
    c = 1

#TESTE
"""print(alunos)
print(alunos[0][0])
print(len(alunos))"""

"""soma = (alunos[0][1]+alunos[0][2])/2
print(soma)
alunos[0].append(soma)
print(alunos)

del soma
soma = (alunos[1][1]+alunos[1][2])/2
print(soma)
alunos[1].append(soma)
print(alunos)

"""

for itens in range(0, len(alunos)):
    alunos[itens][0].upper()
    media = (alunos[itens][1] + alunos[itens][2])/2
    alunos[itens].append(media)
    del media

print('=-'*30)
print('No.  Nome                 MÉDIA')
print('-'*25)

for pos, itens in enumerate(alunos):
    print(f'{pos+1:<}  {itens[0]:>7}                {itens[3]}')

print('\n')

while True:
    opcao = int(input('Mostrar notas de alunos referente ao numero da Tabela:?'))
    print(f'Notas de {alunos[opcao][0]} é:AV1-{alunos[opcao][1]} e AVI-{alunos[opcao][2]}')
    opcao2 = str(input('Deseja continuar?S/N')).strip().upper()
    while opcao2 not in 'SN':
        opcao2 = str(input('Deseja continuar?S/N:')).strip().upper()

    if opcao2 == 'N':
        break



