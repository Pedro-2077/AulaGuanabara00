#LISTA PARTE2

teste = list()
teste.append('Maria')
teste.append(25)

galera = list()
galera.append(teste[:])

print(galera)

#VAMOS NOS DEPARA COM UM PROBLEMA CASO VOCE CRIE OUTRA LISTA DENTRO DO GALERA COM SEM COLOCA [:] ELE VAI COPIAR TUDP EX

teste[0] = 'Joao'
teste[1] = 21

galera.append(teste[:])
print(galera)

#COMO VISTO ELE ACABOU COPIANDO PARA ISSO NAO ACONTECER COLOQUE [:]

teste[0] = 'Marcos'
teste[1] = 35

galera.append(teste[:])
print(galera)

#COMO DECLARA A LISTA

pessoas = [['Joao', 19], ['Ana', 25], ['Maria', 33], ['Pedro', 22]]
print(f'DECLARANDO MATRIZ: {pessoas}')

#SE EU QUISER UM VALOR ESPECIFICO

print(f'POSIÇÂO ESPECIFICA DE ALGO: {pessoas[1][0]}')
print('\n')
for p in pessoas:
    print(f'{p}')#PARA CADA INDICE DENTRO DO VETOR PRINT ISSO LEMBRESE DISSO

#DA PRA FAZER ASSIM

for p in pessoas:
    print(f'{p[0]} tem {p[1]} idades')

#FIXANDO

galeras = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Digite seu nome:')))
    dado.append(int(input('Digite sua idade:')))
    galeras.append(dado[:])
    dado.clear()

print(galeras)

maior18 = 0
menor18 = 0

for p in galeras:
    if p[1] >= 21:
        print(f'Pessoa {p[0]} maior de idade')
        maior18 += 1
    else:
        print(f'Pessoa {p[0]} menor de idade')

print(f'A quantidade de maiores de idades é {maior18}')
print(f'A quantidade de menores de idades é {menor18}')
