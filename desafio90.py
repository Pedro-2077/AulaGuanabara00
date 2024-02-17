print('===== DESAFIO 90 =====')

alunos = []
pessoa = {}
qtd = 0

qtd = int(input('Digite a quantidade de alunos:'))

for c in range(0, qtd):
    pessoa['nome'] = str(input('Digite o nome do aluno: '))
    pessoa['media'] = float(input('Digite a media do aluno: '))
    if pessoa['media'] >= 6:
        pessoa['situacao'] = 'Aprovado'
    else:
        pessoa['situacao'] = 'Reprovado'

    alunos.append(pessoa.copy())

print('=-'*30)
print(f'{alunos}')

for i in alunos:
    for k,v in i.items():
        print(f'{k} é igual: {v}')
