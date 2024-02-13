import math
angulo = float(input("Digite o angulo: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print('O resultado é:')

print('Seno:{:.2f}\nCosseno{:.2f}\nTangente{:.2f}'.format(sen, cos, tg))

