#Ordem de Precedencia

#1 ()
#2 **
#3 * / // %
#4 + -

#Teste Raiz quadrada

numero = int(input('Digite um numero:'))

raiz = numero ** (1/2)
cubica = numero **(1/3)

#colocando limitador na casas decimais EX
print('A raiz quadrada é:{:.2f}'.format(raiz))
print('A raiz cubica é:{:.3f}'.format(cubica))

#Uma curiosidade é que o pythin aceita numeros gigantes vai depender da sua ram

numero = 10**20

print(numero)

#Como descobri o tipo primitivo

#Type

print(type(numero))

#posso multiplicar as repetições de string EX

print('='*20)
print('='*25)

#centralizando caracteres e alinhando

nome = input('Digite seu nome:')
print('Prazer em te conhecer {:20}!'.format(nome))
#Centralizar

print('Prazer em te conhecer {:^20}!'.format(nome))

#Direita
print('Prazer em te conhecer {:>20}!'.format(nome))

#colocando coisas no espaço
print('Prazer em te conhecer {:=^20}!'.format(nome))

#Coloando dois prints com end

print('Ola mundo', end=' ')
print('Prazer em te conhecer ', nome)

#Adicionando no end

print('Ola mundo ', end=' >>>>> ')
print('Juntando com end')





