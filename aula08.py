import math
import random
#Aula 09

#Importando biblioteca Math

#ceil arredondada pra cima
#floor arredonda para baixo
#trunc tira os decimais
#pow eleva a potencia
#sqrt raiz quadrada
#factorial fatorial calculo


# Detalha para importa uma biblioteca tem que da um import no inicio do programa e depois da o nome referente a biblioteca

#import math como vemos la emcima
#nesse caso ele vai importa tudo da biblioteca EX

#EX: from math import sqrt // from math import sqrt,ceil (nesse caso estou importanto dois metodos)

#PRATICANDO

numero = int(input('Digite um numero:'))
raiz = math.sqrt(numero)

print('A raiz {} é:{}'.format(numero, math.ceil(raiz))) #Poderia utila o from math import sqrt,ceil

#biblioteca random

#random
num = random.random() #Aqui ele vai me da um numero aleatorio entre 0 e 1

print(num)

#randint

num2 = random.randint(1,20)#numero aleatorio inteiro entre 1 e 20
print(num2)

#tem como baixar tambem bibliotecas e so escolher uma biblioteca que, voce pode encontrar no site do python
#e depois disso e so aperta na lanterna e instalar



