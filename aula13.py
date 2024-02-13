#FOR LAÇO DE REPETIÇÂO

for c in range(0,15):
    print('Me mama')
print('FIM da mamada')

for c in range(0,5):
    print(c) #Se eu fala para printar o c ele vai conta do 0 a 5 é como se fosse o i de index

for c in range(6,0,-1):#Aqui eu coloco invertido e peço para conta -1 adicionando esse termo depois do 0 que e a variavel de controle
    print(c)

for c in range(0,10,2):#Aqui ele vai pular de dois em dois o utlimo funciona como contador ou decrementando um numero
    print(c)

#Da para fazer de outro jeito:

fim = int(input('Digite um numero:'))

for c in range(0,fim):#Vai conta do inicio ao fim que voce digitou no input
    print(c)

inicio = int(input('Digite o inicio:'))
pulando = int(input('Digite o pulando:'))

for c in range(inicio,fim+1,pulando):#AQUI EU ESCOLHI O INICIO E O PULO O INCREMENTO / ADICIONEI MAIS 1 para ir ate o numero digitado
    print(c)


s = 0
for c in range (0,4):
    n = int(input('Digite um numero:'))
    s += n
print(s)