#LISTAS

#APPEND (ADICIONA na lista)
lanche = ['Hamburguer', 'abacate', 'Suco', 'Pizza', 'Pudim']
lanche.append('biscoito')#

#EX
print('Append adicionando BISCOITO', lanche)

#INSERT (ADICIONA ALGO A LISTA ONDE VOCE QUISER)

lanche.insert(0,'chocolate')
print(f'\n\nESSA LISTA COM INSERT POSIÇÂO 0 com a palavra CHOCOLATE:\n{lanche}')

lanche.insert(2, 'Abacaxi')
print(f'COM OUTRO INSERT: {lanche}')

#APAGANDO ALGO DA LISTA

#DEL
#POP SEM PARAMETRO APAGA O ULTIMO DA LISTA
#REMOVE NO CASO VOCE SO REMOVE PELO VALO DA INDICE E SE TIVER INDICE COM O MESMO VALOR ELE VAI REMOVER O PRIMEIRO QUE ACHAR EM ORDEM CRESCENTE DA INDICE

#EX

del lanche[3]
print(f'DELETE 3 indice com o del: {lanche}')
lanche.pop(3)
print(f'DELETE 3 indice com o POP: {lanche}')
lanche.remove('Pizza')
print(f'DELETE 3 indice com o remove: {lanche}')

#USANDO O POP SEM PARAMETRO VAI TIRAR A ULTIMA INDICE

lanche.pop()
print(f'DELETE ultima indice com o POP: {lanche}')

#REMOVENDO COM IF CASO TENHA ALGO NA LISTA

if 'Hamburguer' in lanche:
    lanche.remove('Hamburguer')
print(f'\n\nESSA LISTA COM o HAMBURQUE RETIRADO:\n {lanche}')

#CRIANDO LISTA COM RANGE

valores = list(range(10, 0, -1)) #CRIANDO UMA LISTA COM RANGE
print(valores)

#SORTED ORDENANDO A LISTA

valores.sort()
print(valores)

#REVERSE ODENADO DE BAIXO PARA CIMA

valores.reverse() #ou valores.sort(reverse=True)
print(valores)

# E TEMOS O LEN

#CRIANDO UMA LISTA

numero = [] ## OU ASSIM numero = list()
numero.append(10)
numero.append(14)
numero.append(11)

for v in numero:
    print(f'{v} ', end='')

for c, v in enumerate(numero):
    print(f'\nO valor {v} esta na posição {c} ', end='')

#ADICIONANDO VALORES NUM LOOP
valor = []
for var in range(0, 3):
    valor.append(int(input('\nDigite um valor:')))
print(valor)

'''TEM ALGO MUITO IMPORTANTE A SE FIXA OLHE NO EXEMPLO ABAIXO DO PROGRAMA'''

a = [1, 2, 3, 4]
b = a
print(b)

"""SE EU MUDAR A LISTA B ADICIONANDO OU REMOVENDO OU ATE ALTERANDO VOCE TAMBEM VAI ALTERQA A LISA A
   PQ AS LISTA QUANDO VC IGULA ELAS FICAM INTERLIGADAS EX ABAIXO
"""

b.insert(0, 5)
print('LISTA A=',a)
print('LISTA B=',b)

'''POREM TEM COMO BURLAR ISSO È SO VOCE PEDIR PARA ELE COPIAR OS VALORES (ITENS) NAO AS INDICES JUNTO '''

d = [9, 4, 5, 3, 8]
e = d[:]#AQUI ESTOU DIZENDO PARA COPIAR SO OS ITENS ISSO VAI FAZER COM QUE O E SE ALTERE MAIS NAO ALTERE JUNTO O D
d[2] = 4

print(f'{d} \n{e}')
