#DICIONARIO

#DECLARANDO

dados = dict() #OU  dados = {}

#COMO COLOCO OS DADOS DENTRO DA ESTRUTURA

                #PEDRO È O VALOR
dados = {'Nome': 'Pedro', 'Idade': 25}
        #NOME È O IDENTIFICADOR

# SE EU DA UM PRINT NOS DADOS NOM, NO CASO NAO È 0 MAIS SIM NOME

#VAI PRINTAR O NOME QUE ESTA NA PARTE NOME
print(dados['Nome'])
print(dados['Idade'])

#COMO ADICIONA

dados['sexo'] = 'M'
print(dados)#VIMOS QUE ADICIONOU NA ULTIMA POSIÇÂO

#ELIMINA ELEMENTO

del dados['Idade']
print(dados)#AQUI NOS CONSEQUIMOS VER QUE ELE A IDADE DA LISTA

#OUTRO EXEMPLO

filme = {'titulo': 'Star Wars', 'ano': 1977, 'Diretor': 'George Lucas'}
                    #TITULO         #ANO            #DIRETO
#O PYTHON CHAMA O ELEMENSTOS TITULO, ANO,DIRETOR DE KEYS(CHAVES)
#PARA PEGAR

#PRINTANDO SO A PARTE DO VALORES(VALUES)
print(filme.values())

#PRINTANDO SO AS CHAVES(KEYS) QUE SAO OS NOMES QUE VOCE DESEGNA PRA CADA COISA
print(filme.keys())

#PRINTANDO OS DOIS ITEMS(ITEMS)
print(filme.items())

#FAZENDO COM FOR

for keys, values in filme.items():#AQUI ELE VAI PEGAR O KEYS QUE SAO AS CHAVES E O VALORES E PRINTAR CADA
    print(f'{keys}: {values}')

#PODEMOS TBM COLOCAR DICIONARIOS EM LISTA

#LOCADORA
locadora = list()

locadora.append(filme)
print(locadora)

#O DICIONARIO FICOU DENTRO DA LISTA

#POSSO PRINTAR ASSIM

print(locadora[0]['ano']) #VAI PRINTAR 1977

#PRATICA

pessoas = {'Nome': 'Pedro', 'Idade': 25, 'Sexo': 'M'}
print(pessoas)
print(pessoas['Nome'])#NAO PODE SER PESSOAS 0 MAIS SIM NOME, COMO VOCE COLOCOU

#PRINT FORMATADO

print(f'O {pessoas['Nome']} tem {pessoas['Idade']} anos')

#PRINTADO SO A CHAVES

print(pessoas.keys())

#PRINTANDO NO FOR
#PRINTANDO SO AS KEYS
for k in pessoas.keys():#FAZENDO DE PESSOAS VIRA K
    print(f'{k}')

for k in pessoas.values():#FAZENDO SO OS VALORES PRINTAR
    print(f'{k}')

for v, k in pessoas.items():#PRINTANDO OS DOIS TEM QUE COLOCAR DUAS VAREAVEIS
    print(f'{v} = {k}')

#SE EU APAGAR O SEXO

del pessoas['Sexo']

print('\n')
for k, v in pessoas.items():
    print(f'{k} = {v}')

#PODEMOS MODIFICAR UM VALOR NO DICIONARIO

pessoas['Nome'] = 'ERICK'
print(pessoas)

#POSSO ADICIONAR

pessoas['Peso'] = 85

print(pessoas)

#CRIANDO NOVAMENTE UM LISTA COM DICIONARIO

brasil = list()
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}

brasil.append(estado2)
brasil.append(estado1)

print(brasil)

#MOSTRANDO SÒ UM VALOR ESPECIFICO

print(brasil[0]['Sigla'])#VAI PRINTAR

estado = dict()
brasil = list()

#UTILIZANDO O COPY() NÂO DA MAIS PARA FATIAR COMO SE FAZIA NA LISTA [:]
for c in range(0, 2):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Digite a Sigla do Estado: '))
    brasil.append(estado.copy())

print(brasil)

print('\n')

#FAZENDO ISSSO ELE VAI PASSA POR CADA ITEM E VALOR DA LISTA
for e in brasil: #PARA CADA ITENS NA LISTA BRASIL
    for k, v in e.items():#E PARA CADA CHAVE E VALOR, DIZEND QUE QUERO ITEMS NO CASO OS DOIS
        print(f'{k} = {v}')


#SO OS VALORES
for e in brasil:#PARA CADA INDICE EM BRASIL
    for v in e.values():#PARA CADA VALOR DAS INDICES DO BRASIL ELE VAI PEGAR CADA VALOR DO BRASIL
        print(f'{v}',end= ' ')



