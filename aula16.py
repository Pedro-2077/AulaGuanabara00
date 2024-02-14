#PRATICA
#TUPLAS

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim' )

print(lanche[1])
print(lanche[2:])
print(lanche[1:])
print(lanche[-3:])

#TUPLAS SÂO IMUTAVES EX

#lanche[2] = 'Sorvete' ISSO NAO FUNCIONA TUPLA È IMUTAVEL

#Printando tudo ta tupla

#PODE SER FEITO DE DUAS MANEIRAS

for c in lanche: #USANDO A VARIAVEL COMPOSTA
    print(f'eu vou come {c}')
print('\n\n')

for c in range(0, len(lanche)): #OU USANDO O RANGE E USAR O C COMO SE FOSSE INDEX I
    print(f'eu vou come {lanche[c]} na posição {c}')
print('\n\n')

for cont, c in enumerate(lanche):#AQUI EU USO UM METODO ENUMERATE PARA CONTAR AS VEZES  E O C PARA SER O LANCHE
    print(f'eu vou comer {c} na posição {cont} ')

#METODO PARA ORGANIZAR A TUPLA

#SORTED
print(sorted(lanche))#AQUI O SORTED ORGANIZA MAIS NAO MUDOU A TUPLA

print('\n\n')

#JUNTADO TUPLAS
a = (1, 2, 3, 4, 2)
b = (5, 6, 7, 8)
c = a+b

print(c)

#PODEMOS VER QUANTAS OCORRENCIAS ACONTECE NUMA TUPLA

#COUNT

print(c.count(2))#AQUI ELE VAI ME DIZER QUANTAS VEZES APARECE O NUMERO ENTRE PARENTESES NO COUNT

#VENDO A POSIÇÂO

#INDEX

print(c.index(6))#VENDO A INDICE DO NUMERO DESEJADO A PRIMEIRA OCORRENCIA

print(c.index(2,2))#AQUI ELE VAI ME DA A INDICE APARTI DA POSICIAÇ STARTADA QUE EU ESCOLHE

#TUPLAS COM TIPOS PRIMITIVOS DIFERENTES

pessoa = ('PEDRO', 18, 'M', 78.5)#VARIOS TIPOS PRIMITIVOS DIFERENTE

print(pessoa)

#APAGANDO VARIAVEL E TUPLAS

#DEL

del(pessoa)

print('printando>>>', pessoa) #NAO VAI PRINTAR A TUPLA


