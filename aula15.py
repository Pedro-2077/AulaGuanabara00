#LAÇOS INFINITOS E QUEBRA DE WHILE
s=0
while True:
    n = int(input('Digite um numero:'))
    if n == 999:
        break
    s = s+n

print(f'A soma dos numeros é {s}')

#OUTRO EXEMPLO / F STRINGS

idade = 15
nome = 'Pedro'
salario = 1250.7052
print(f'O seu nome {nome} e sua idade {idade} ')

print(f'Seu nome é {nome:-^20} e sua idade {idade} e seu salario é salario {salario:.2f}') ### Tudo que usamos podemos usar aqui
