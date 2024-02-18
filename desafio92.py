import datetime

print('====== DESAFIO 92 ======')

INSS = []
dados = {}
idade = 0

while True:
    dados['Nome'] = str(input('Digite seu nome:'))
    idade = int(input('Digite seu Nascimento:'))
    dados['CTPS'] = int(input('Carteira de Trabalho (0 nã tem):'))
    if dados['CTPS'] == 0:
        INSS.append(dados.copy())
        break
    else:
        idade = datetime.date.today().year - idade
        dados['Idade'] = idade
        dados['ano-Contratação'] = int(input('Ano de de Contratação:'))
        dados['Salario'] = float(input('Salário: R$'))
        dados['Sexo'] = str(input('Digite seu sexo [M/F]:')).strip().upper()
        if dados['Sexo'] == 'M':
            dados['Aposentadoria'] = (65 - idade) + datetime.date.today().year
        elif dados['Sexo'] == 'F':
            dados['Aposentadoria'] = (62 - idade) + datetime.date.today().year
        INSS.append(dados.copy())
        op = input('Deseja continuar?[S/N]:').strip().upper()[0]
        while op not in 'SN':
            op = input('Deseja continuar?[S/N]:').strip().upper()[0]
        if op in 'SN':
            break
print(INSS)

for linha in INSS:
    for k, v in linha.items():
        print(f' - {k} tem o valor {v}')




