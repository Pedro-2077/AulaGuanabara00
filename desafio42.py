print('===== DESAFIO 42 =====')
triangulo = bool

r1 = float(input('Digite a primeira reta:'))
r2 = float(input('Digite a segunda reta:'))
r3 = float(input('Digite a terceira reta:'))

if (r1+r2) > r3 and (r1+r3) > r2 and (r2+r3) > r1:
    print('Os segmentos podem forma um triangulo')
    triangulo = 'True'
else:
    print('Os segmentos não podem forma um triangulo')

if triangulo == 'True' and r1 == r2 and r1 == r3 and r2 == r3:
    print('O triagulo é equilátero')

elif triangulo == 'True' and r1 != r2 and r1 != r3 and r2 != r3:
    print('O triangulo é Escaleno')

elif triangulo == 'True':
    print('O triangulo é Isósceles')

#OUTRA FORMA DE FAZER
print('\n\n\n')

s1 = float(input('Digite o primeiro segmento:'))
s2 = float(input('Digite o segundo segmento:'))
s3 = float(input('Digite o terceiro segmento:'))

if (s1+s2) > s3 and (s1+s3) > s2 and (s2+s3) > s1:
    print('Os segmentos podem forma um triangulo')
    if s1 == s2 == s3: #O python aceita igualdade dessa maneira
        print('Esse triangulo equilatero')
    elif s1 != s2 != s3 != s1: print('Esse triangulo escaleno') #Aqui teve que fazer a diferença entre todos
    else:print('Esse triangulo é Isósceles')
else:
    print('Os segmentos não podem forma um triangulo')