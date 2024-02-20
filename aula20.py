#Função

#DEF
#CRIANDO FUNÇÂO:
def linha():
    print('-'*30)


def mensagem(txt):
    print(txt)


linha()
print(' O Sistema de Aula Python')
linha()
mensagem('Me mama')


#VARIOS VALORES
def contador(*n):
    print(f'Recebe {n} valores')


contador(1, 5, 3, 4)
contador(2, 5, 8, 2)

#Função com Lista

def dobra(lst):
    index = 0
    while index < len(lst):
        lst[index] *= 2
        index+=1


valores = [7, 5, 6, 3]
dobra(valores)
print(valores)


#SOMA TUPLAS

def soma(*valores):
    soma = 0
    for valor in valores:
        soma += valor
    print(f'Somando os valores {valores} temos {soma}')


soma(5, 6)
soma(4, 5, 7, 2)
