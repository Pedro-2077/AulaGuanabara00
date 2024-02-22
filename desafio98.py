from time import sleep
def calculo(num, num2, num3):
    if num3 == 0:
        num3 = 1
    while num >= num2:
        num -= num3
        print(num)
        sleep(0.5)

    while num < num2:
        num += num3
        print(num)
        sleep(0.5)


print('-='*30)
for c in range(1, 11):
    print(f'{c}',end=' ')
    sleep(0.5)
print()
print('-=' * 30)

for c in range(10, 0, -2):
    print(f'{c}', end=' ')
    sleep(0.5)
print()
print('-=' * 30)

n1 = int(input('Digite o valor do inicio:'))
n2 = int(input('Digite o valor fim:'))
passo = int(input('Digite os pulos:'))
calculo(n1, n2, passo)
